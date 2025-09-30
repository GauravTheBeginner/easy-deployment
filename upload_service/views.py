from rest_framework import generics
from upload_service.serializers import ProjectSerializer 
from upload_service.models import Project
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from common.models import User
from common.s3 import create_s3_folder_and_upload_file
from common.utils import getfolder, getAllFiles, generateSessionID
import uuid
import os
from git import Repo
from rest_framework.views import APIView
from rest_framework.response import Response
from upload_service.redis_status import get_upload_status

class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        #step 0: Extract repo_url and user_id from request data
        repo_url = request.data.get('repo_url')
        user_id = request.data.get('user')

        #step 1: Validate user (id=user_id)
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
        
        #step 2: Generate unique session ID and create output directory
        project_id = generateSessionID()

        #step 3: Path to checkout repository folder exist or create new
        out_dir = os.path.join('out', project_id)
        os.makedirs(out_dir, exist_ok=True)
        print(f"Output directory created at: {out_dir}")
        #step 4: Clone the repository and add into out directory
        try:
            Repo.clone_from(repo_url, out_dir)
        except Exception as e:
            return Response({'error': f'Git clone failed: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

        #step 5: List all files of cloned repository in out directory
        folder_structure = getfolder(out_dir)
        print(f"Cloned repository folder structure: {folder_structure}")
        files = getAllFiles(folder_structure)
        print(f"Cloned repository files: {files}")

        #step 6: add all files into s3 (Celery background tasks)
        for file_path in files:
            create_s3_folder_and_upload_file(
                bucket=os.getenv('BUCKET_NAME'),
                project_id=project_id,
                out_dir=out_dir,
                local_file_path=file_path
            )

        # step 6: Create Project instance and return response
        project = Project.objects.create(
            user=user,
            repo_url=repo_url,
        )
        serializer = ProjectSerializer(project)
        return Response({'id': str(project.id), 'project': serializer.data,"sessionID": str(project_id)}, status=status.HTTP_201_CREATED)

class ProjectRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

class ProjectDeleteView(generics.DestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)
    


class UploadStatusView(APIView):
    def get(self, request, session_id):
        status = get_upload_status(session_id)
        if status:
            return Response({"session_id": session_id, "status": status.decode()})
        else:
            return Response({"session_id": session_id, "status": "not found"}, status=404)
