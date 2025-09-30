from django.urls import path, include
from rest_framework.routers import DefaultRouter
from upload_service.views import (
    ProjectListCreateView,
    ProjectRetrieveUpdateView,
    ProjectDeleteView,
    UploadStatusView
)


router = DefaultRouter() 
urlpatterns = [
    path('', include(router.urls)),
    path('deploy/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('deploy/<uuid:pk>/', ProjectRetrieveUpdateView.as_view(), name='project-retrieve-update'),
    path('deploy/<uuid:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('upload-status/<str:session_id>/', UploadStatusView.as_view(), name='upload-status'),
]
