from django.contrib.auth.models import User

__author__ = 'hongleviet'
# myapp/api.py
from tastypie.resources import ModelResource
from ignite.models import *
from tastypie import fields



class CompanyResource(ModelResource):
    class Meta:
        queryset = Company.objects.all()
        resource_name = 'company'

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
