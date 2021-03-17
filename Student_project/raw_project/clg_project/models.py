from django.db import models

# Create your models here.
class poject(models.Model):
    def __str__(self):
        return self.project_name
    project_name=models.CharField(max_length=200)
    project_price=models.IntegerField()
    project_author=models.CharField(max_length=200)
    project_description=models.TextField()
    project_image=models.CharField(max_length=500,default="https://th.bing.com/th/id/OIP.WcPTltgdtoFyOmeQHPsEvgHaHa?pid=Api&rs=1")