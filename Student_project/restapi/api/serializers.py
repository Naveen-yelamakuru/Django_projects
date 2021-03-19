from rest_framework import serializers 
from .models import moviedata


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=moviedata
        fields=['id','name','duration','rating']