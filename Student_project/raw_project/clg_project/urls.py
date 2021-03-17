from . import views
from django.urls import path

app_name='clg_project'
urlpatterns = [
    path('',views.index,name='index'),
    path('naveen/',views.naveen,name='naveen'),
    path('poject1/',views.poject1,name='poject1'),
    path('<int:project_id>/',views.details,name='details'),
    # add items
    path('add/',views.add_project,name='add_project'),
    # edit items
    path('edit/<int:id>/',views.edit_project,name='edit_project')
    # delete items
   # path('delete/<int:id>/',views.delete_project,name='delete_project')
]