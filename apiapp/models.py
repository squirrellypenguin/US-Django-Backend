from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=300)
    summary = models.TextField(max_length=1000, help_text='What is what')
    url = models.CharField(max_length=300, help_text='To Store Img', null=True, default="Aspirational",)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    lat = models.FloatField(default=0)
    latRef = models.CharField(max_length=1, default='X')
    long = models.FloatField(default=0) 
    longRef = models.CharField(max_length=1, default='X')
    def __str__(self):
        return self.title