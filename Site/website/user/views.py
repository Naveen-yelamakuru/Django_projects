from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.db.models import Avg,Sum,Max,Min,Count 
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Calculation

# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,'welcom {}'.format(username))
            return redirect('list')
    else:
        form=RegisterForm()
    return render(request,'user/register.html',{'form':form})

@login_required
def userprofile(request):
    return render(request,'user/profile.html')
def practice(request):
    # data=Calculation.objects.all()
    # data=Calculation.objects.all()[0:2]
    # data=Calculation.objects.values('name','salary')
    # data=Calculation.objects.create(name='prasad',salry=100,address='narpala')
    # data=Calculation.objects.get(name__exact='naveen')
    # data=Calculation.objects.filter(address='kadiri')
    # result=[data.name,data.salary,data.address]
    # data=Calculation.objects.filter(name__contains='n')
    # data=Calculation.objects.filter(salary__gt=22000)
    # data=Calculation.objects.filter(salary__gte=22000)
    # data=Calculation.objects.filter(salary__lt=22000)
    # data=Calculation.objects.filter(salary__lte=22000)
    # data=Calculation.objects.exclude(salary__gte=22000)
    # data=Calculation.objects.filter(id__in=[1,2])
    data=Calculation.objects.all().aggregate(Min('salary'))
# asecending order
    # data=Calculation.objects.all().order_by('name')
# descending order
    # data=Calculation.objects.all().order_by('-name')

    # it apply whole data set
    # data=Calculation.objects.values('salary').annotate(sum('salary'))
    #update values
    #data=Calculation.objects.update(age=F('salary')*2)
    # data=Calculation.objects.get(id=1)
    #data.salary=1000
    #data.save()
    #Calculation.objects.all().delete()
    #data=Calculation.objects.get(id=4)
    #data.delete()
    #data=Calculation.objects.filter(address='kadiri') & Calculation.objects.filter(name='manoj')


    return HttpResponse(data)
    

    # return render(request,'user/practice.html',{'data':data})

