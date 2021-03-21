from django.shortcuts import render
from .models import data
import requests
import bs4
from django.http import HttpResponseRedirect

# Create your views here.

def display(request):
    if request.method == "POST":
        site = request.POST.get('site','')
        result = requests.get(site)
        soup=bs4.BeautifulSoup(result.text,'lxml')
        links=soup.find_all('div',attrs={'class':'topStories lftBlk flt'})
        for a in links[0].find_all('h2'):
            link_text=a.text
            link_address='https://economictimes.indiatimes.com/'+a.a['href']
            data.objects.create(link=link_address,data=link_text)
        return HttpResponseRedirect('/')
    else:
        data1 =data.objects.all()
 
 
    return render(request,'link/result.html',{'data1':data1})

def clear(request):
    data.objects.all().delete()
    return render(request,'link/result.html')
