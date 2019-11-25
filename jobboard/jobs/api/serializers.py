from rest_framework import serializers
from jobs.models import JobPost, JobTag, Company


class JobTagSerializer(serializers.ModelSerializer):



    class Meta:
        model = JobTag
        fields = "__all__"


class JobPostSerializer(serializers.ModelSerializer):

    tags = JobTagSerializer(many=True, read_only=True)
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = JobPost
        fields = "__all__"

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_updated_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")



class CompanySerializer(serializers.ModelSerializer):

    company_job = JobPostSerializer(many=True, read_only=True)
    class Meta:
        model = Company
        fields = "__all__"
