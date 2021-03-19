from django.shortcuts import redirect,render
from django.http import HttpResponse
from .models import Properites
from django.template import loader
from .forms import vechileForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
# sample views and learning urls
# it is a function view


def StartPage(request):
    vechile=Properites.objects.all()
    context= {
        'vechile':vechile,
    }
    return render(request,'vechiles/startpage.html',context)
    # class based view    
class IndexClassView(ListView):

    model=Properites
    template_name ='vechiles/startpage.html'
    context_object_name='vechile'


    #return HttpResponse(vechile)
def first(request):
    return HttpResponse("jantu college")

def details(request,id):
    vechile=Properites.objects.get(pk=id)
    context={
        'vechile':vechile
    }
    return render(request,'vechiles/details.html',context)


class detailclassview(DetailView):
    model=Properites
    template_name='vechiles/details.html'
    

def add_data(request):
        # create object for form class in forms.py
    form=vechileForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('vechiles:StartPage')
    return render(request,'vechiles/vechileform.html',{'form':form})
def update(request,id):
    vechile=Properites.objects.get(id=id)
    form=vechileForm(request.POST or None,instance=vechile)

    if form.is_valid():
        form.save()
        return redirect('vechiles:StartPage')
    return render(request,'vechiles/vechileform.html',{'form':form,'vechile':vechile})
def delete(request,id):
    vechile=Properites.objects.get(id=id)
    if request.method =='POST':
        vechile.delete()
        return redirect('food:StartPage')
    return render(request,'vechiles/delete.html',{'vechile':vechile})
    








