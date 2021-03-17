from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class calories(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=200)
    carbs=models.FloatField()
    protein=models.FloatField()
    facts=models.FloatField()
    calories=models.IntegerField()
class consum(models.Model):
    # def __str__(self):
    #     return self.user
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    food_consumed=models.ForeignKey(calories,on_delete=models.CASCADE)