from django.db import models
from django.utils.text import  slugify
import uuid
from startups import settings

def get_filestore_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "our-humble-logo/%s.%s" % (uuid.uuid4(), ext)
    return filename


class Category(models.Model):
    name = models.CharField(max_length=255, default="", blank=True)



    def __unicode__(self):
            return self.name


# Create your models here.



class Person(models.Model):
    name = models.CharField(max_length=255, default="", blank=True)
    email = models.CharField(max_length=255, default="", blank=True)
    bio = models.TextField( default="", blank=True)

    def __unicode__(self):
            return self.name



class Company(models.Model):
    name = models.CharField(max_length=255, default="", blank=True)
    category = models.ForeignKey(Category)
    founding_year = models.IntegerField(null= True, default=2013, blank= True)
    founding_month = models.IntegerField(null= True, default=1, blank= True)
    founding_day = models.IntegerField(null= True, default=1, blank= True)
    one_sentence_description = models.CharField(max_length=256, default="")
    description = models.TextField(default= "")
    phone = models.CharField(max_length=256, default="")
    email = models.CharField(max_length=256,default="")
    address = models.CharField(max_length=256,default="")
    website = models.CharField(max_length=256,default="")
    logo = models.FileField(blank= True, null= True,upload_to=get_filestore_path)

    founders = models.ManyToManyField(Person, through="Founder")

    def get_logo(self):
        return settings.S3STATIC_URL + str( self.logo)

    def __unicode__(self):
            return self.name

    def get_url(self):
        return "/company/" + str(self.id) + "-" + slugify(self.name) + "/"


class TeamMember(models.Model):
    member = models.ForeignKey(Person)
    company = models.ForeignKey(Company)


class Founder(models.Model):
    founder = models.ForeignKey(Person)
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=255, default="", blank=True)


