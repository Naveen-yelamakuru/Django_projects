from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator



# Create your views here.
def index(request):
    product_objects=Products.objects.all()
    # search operation code
    product_name=request.GET.get('product_name')
    if ((product_name != '') and (product_name is not None)):
        product_objects=product_objects.filter(title__icontains=product_name)
    # code for pagination
    paginator=Paginator(product_objects,1)
    page=request.GET.get('page')
    product_objects=paginator.get_page(page)

    return render(request,'shop/index.html',{'product_objects':product_objects})
def details(request,id):
    product_objects=Products.objects.get(pk=id)
    return render(request,'shop/details.html',{'product_objects':product_objects})
def checkout(request):
    return render(request,'shop/checkout.html')
