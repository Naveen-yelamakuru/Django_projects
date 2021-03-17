from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='profile.jpg',upload_to='profile_pictures')
    location=models.CharField(max_length=200)
    def __str__(self):
        return self.user.username

class Calculation(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=200)
    salary=models.IntegerField()
    address=models.CharField(max_length=200)
