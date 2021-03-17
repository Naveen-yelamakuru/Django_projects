from rest_framework import serializers
from home.models import Provider
class providerserializer(serializers.ModelSerializer):
    class Meta:
        model=Provider
        fields=['company','address','country','manufactured']
 
