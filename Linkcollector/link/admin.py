from django.contrib import admin
from .models import Link

# Register your models here.
class adminmodel(admin.ModelAdmin):
    list_display=['name','address']

admin.site.register(Link,adminmodel)
