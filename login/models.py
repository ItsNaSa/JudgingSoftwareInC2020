from django.db import models
from django.conf import settings


# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

