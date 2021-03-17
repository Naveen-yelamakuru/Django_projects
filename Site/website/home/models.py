from django.db import models

# Create your models here.

class Home(models.Model):
    def __str__(self):
        return self.name
    
    name=models.CharField(max_length=200)
    price=models.FloatField()

class Provider(models.Model):
    def __str__(self):
        return self.company
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    company=models.CharField(max_length=200)
    address=models.TextField()
    country=models.CharField(max_length=200)
    manufactured=models.DateField()
    
