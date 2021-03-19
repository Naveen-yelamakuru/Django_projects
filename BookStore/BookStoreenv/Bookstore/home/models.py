from django.db import models

# Create your models here.

class employee(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=200)
    profile=models.CharField(max_length=200)
    company=models.CharField(max_length=200,default='tcs')
    description=models.CharField(max_length=200)
    salary=models.FloatField()
class personal_details(models.Model):
    date_of_join=models.DateField(default='20-04-17')
    emp=models.ForeignKey(employee,on_delete=models.SET_NULL,null =True)
    