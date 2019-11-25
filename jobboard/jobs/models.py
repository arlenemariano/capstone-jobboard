from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    members = models.ManyToManyField(User,
                            through='CompanyMember',
                            through_fields=('company', 'member',))

    def __str__(self):
        return self.name

class CompanyMember(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)

class JobTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class JobPost(models.Model):
    LOC_REMOTE = 'REM'
    LOC_ONSITE = 'ONS'

    STS_DRAFT = 'DRF'
    STS_PUBLISHED = 'PUB'
    STS_CLOSED = 'CLO'
    STS_EXPIRED = 'EXP'

    LOCATION_TYPE_CHOICES = (
        (LOC_REMOTE, 'Remote',),
        (LOC_ONSITE, 'On-site',),
    )

    STATUS_CHOICES = (
        (STS_DRAFT, 'Draft',),
        (STS_PUBLISHED, 'Published',),
        (STS_CLOSED, 'Closed',),
        (STS_EXPIRED, 'Expired',),
    )

    title = models.CharField(max_length=60)
    description = models.TextField()
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                related_name="company_job")
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    location_type = models.CharField(max_length=3)
    location = models.CharField(max_length=70)
    tags = models.ManyToManyField(JobTag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
