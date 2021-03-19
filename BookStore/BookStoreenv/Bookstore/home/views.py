from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.generic.list import ListView
from .models import employee
from django.core.serializers import serialize
# from .mixin import mixed

# Create your views here.
# def employee(request):
#     details={
#         "name":'naveen',
#         "address":'anantapur',
#         "salary":30000
#     }
#     # resp={'name{} address{},salary{}'.format(details['name'],details['address'],details['salary'])}
#     # return HttpResponse(resp)
#     data=json.dumps(details)
#     return HttpResponse(data)
# class MyView(mixed,View):
#     def get(self, request):
#         return self.mix()
# class details(View):
#     def get(self,request,id,*args,**kwargs):
#         emp=employee.objects.get(id=id)
#         json_data=serialize('json',[emp,],fields=('id','name'))
#         return HttpResponse(json_data,content_type='application/json')

# class listdetails(View):
#     def get(self,request,*args,**kwargs):
#         emp=employee.objects.all()
#         json_data=serialize('json',emp,fields=('id','name'))
#         data=json.loads(json_data)
#         listdata=[]
#         for i in data:
#             listdata.append(i['fields'])
#         json_data=json.dumps(listdata)
#         return HttpResponse(json_data,content_type='application/json')

class list_details(ListView):
    model=employee
    template='home.html'





