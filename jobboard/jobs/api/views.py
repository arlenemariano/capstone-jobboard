from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from jobs.api.pagination import SmallSetPagination


from jobs.api.serializers import JobPostSerializer, JobTagSerializer, CompanySerializer
from jobs.models import JobPost, JobTag, Company


class JobPostListCreateAPIView(generics.ListCreateAPIView):

    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    pagination_class = SmallSetPagination

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ["title", "location", "location_type"]


class JobDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer


class CompanyListCreateAPIView(APIView):

    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


