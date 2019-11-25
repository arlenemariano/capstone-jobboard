from django.urls import path
from jobs.api.views import JobPostListCreateAPIView, JobDetailAPIView

urlpatterns = [
    path("v1/jobs/", JobPostListCreateAPIView.as_view(), name="jobposts-list"),
    path("v1/jobs/<int:pk>", JobDetailAPIView.as_view(), name="jobpost-detail"),
]