from django.contrib import admin
from .models import employee,personal_details

# Register your models here.

class employeeadmin(admin.ModelAdmin):
    list_display=['id','profile','name']

admin.site.register(employee,employeeadmin)
admin.site.register(personal_details)
