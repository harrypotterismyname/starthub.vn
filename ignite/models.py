from django.db import models
from django.utils.text import  slugify

class Category(models.Model):
    name = models.CharField(max_length=255, default="", blank=True)

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255, default="", blank=True)
    category = models.ForeignKey(Category)
    founding_year = models.IntegerField()
    founding_month = models.IntegerField()
    founding_day = models.IntegerField()
    one_sentence_description = models.CharField(max_length=256, default="")
    description = models.TextField(default= "")
    phone = models.CharField(max_length=256, default="")
    email = models.CharField(max_length=256,default="")
    address = models.CharField(max_length=256,default="")
    website = models.CharField(max_length=256,default="")

    def __unicode__(self):
            return self.name

    def get_url(self):
        return "/company/" + str(self.id) + "-" + slugify(self.name) + "/"


class Person(models.Model):
    name = models.CharField(max_length=255, default="", blank=True)

class TeamMember(models.Model):
    member = models.ForeignKey(Person)
    company = models.ForeignKey(Company)


class Founder(models.Model):
    founder = models.ForeignKey(Person)
    company = models.ForeignKey(Company)


