from django.contrib import admin
from .models import Products

# Register your models here.
admin.site.site_header='ATP Online Store'
admin.site.index_title='User Data'
class ProductAdmin(admin.ModelAdmin):
    #change actions
    def change_category_to_default(self,request,queryset):
        queryset.update(description='very good bike')
        queryset.update(price='3000')
    change_category_to_default.short_description='Default Category'


    # if above method name is default then change using below code

    # display the list of data variable names are dont change this are keywords
    list_display=('title','price','discount_price','description',)
    # add search field add any item of like price ,discount_price etc
    search_fields=('title',)
    # add actions
    actions=('change_category_to_default',)
    # add editable fields 
    fields=('category','description',)
    # add editable option in list_group
    list_editable=('price','discount_price',)
admin.site.register(Products,ProductAdmin)
