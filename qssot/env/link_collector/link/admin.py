from django.contrib import admin
from .models import data

# Register your models here.
class details(admin.ModelAdmin):
    list_fileds=['link']

admin.site.register(data,details)
