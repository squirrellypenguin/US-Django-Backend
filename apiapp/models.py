from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=300)
    summary = models.TextField(max_length=1000, help_text='What is what')
    url = models.CharField(max_length=300, help_text='To Store Img', null=True, default="Aspirational",)

class User(models.Model):
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=300)