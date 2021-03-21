from django.db import models

# Create your models here.
class data(models.Model):
    link=models.CharField(max_length=1000,null=True,blank=True)
    data=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.link
