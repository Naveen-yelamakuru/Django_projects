
from rest_framework import generics
from home.models import Provider
from .serializer import providerserializer

# Create your views here.
class homegenerics(generics.ListAPIView):
    serializer_class=providerserializer

    def get_queryset(self):
        return Provider.objects.all()

