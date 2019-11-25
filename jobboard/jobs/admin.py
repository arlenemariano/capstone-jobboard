from django.contrib import admin
from jobs.models import Company, JobPost, JobTag, CompanyMember

admin.site.register(Company)
admin.site.register(JobPost)
admin.site.register(JobTag)
admin.site.register(CompanyMember)
