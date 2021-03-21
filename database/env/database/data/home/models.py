from django.db import models

# Create your models here.

class name(models.Model):
    name=models.CharField(max_length=200)
    display=models.CharField(max_length=200)
