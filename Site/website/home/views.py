from django.shortcuts import render
from .models import Home
from django.http import HttpResponse
import json
from django.core.serializers import serialize
from django.views.generic import ListView,DetailView

# Create your views here.
# class product(ListView):
#     model=Home
#     template_name='home/list.html'
#     context_object_name='data'
def product1(request):
    data=Home.objects.get(id=1)
    jsondata={
        'name':data.name,
        'price':data.price

    }
    d=json.dumps(jsondata)

    return HttpResponse(d,content_type='applictaion/json')
class details(DetailView):
    model=Home
    template_name='home/detail.html'

