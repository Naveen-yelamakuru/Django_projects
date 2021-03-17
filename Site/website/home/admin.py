from django.contrib import admin
from .models import Home,Provider

# Register your models here.
class Homeadmin(admin.ModelAdmin):
    list_display=['name','price']

admin.site.register(Home,Homeadmin)
admin.site.register(Provider)
