from rest_framework import serializers
from upload_service.models import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ["id", "user", "repo_url", "created_at"]