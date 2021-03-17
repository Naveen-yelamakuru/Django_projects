from django.shortcuts import render,redirect
from .models import calories,consum
# from django.contrib.auth.models import User


# Create your views here.
def index(request):
    if request.method=='POST':
        food_consumed=request.POST['food_consumed']
        consume=calories.objects.get(name=food_consumed)
        user=request.user
        consume=consum(user=user,food_consumed=consume)
        consume.save()
        foods=calories.objects.all()
    else:
        foods=calories.objects.all()
    consumed_food=consum.objects.filter(user=request.user)
    
    return render(request,'count/index.html',{'foods':foods,'consumed_food':consumed_food})

def delete(request,id):
    item=consum.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request,'count/delete.html')


