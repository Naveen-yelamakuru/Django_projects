from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import poject
from django.template import loader
from . forms import project_form
# Create your views here.
def index(request):
    return HttpResponse('hello world')
def naveen(request):
    return HttpResponse('<h1>my name is yelamakuru naveen</h1>')
def poject1(request):
    project_list=poject.objects.all()
    #template=loader.get_template('clg_project/poje.html')
    context={
   'project_list':project_list,
    }
    #return HttpResponse(template.render(context,request))
    return render(request,'clg_project/poje.html',context)
def details(request,id):
    poject1=poject.objects.get(id=poject_id)
    context={
    'poject1':poject1,
    }
    #return HttpResponse('naveen')
    return render(request,"clg_project/details.html",context)
def add_project(request):
    form=project_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clg_project:poje')
    return render(request,'clg_project/add_form.html',{'form':form})
def edit_project(request,id):
    project=poject.objects.get(id=id)
    form=project_form(request.POST or None,instance=project)
    if form.is_valid():
       form.save()
       return redirect('clg_project:poje')
    return  render(request,'clg_project/add_form.html',{'form':form})
def delete_project(request,id):
    project=poject.objects.get(id=id)

    if request.method=='POST':
        project.delete()
        return redirect('clg_project:poje')
    return render(request,'clg_project/delete.html',{'poject':poject})


    