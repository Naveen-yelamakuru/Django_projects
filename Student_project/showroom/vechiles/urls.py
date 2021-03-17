from . import views
from django.urls import path

#namespace
app_name='vechiles'
urlpatterns = [
    path('start/',views.IndexClassView.as_view(),name='StartPage'),
    path('college/',views.first,name='first'),
    path('<int:pk>/',views.detailclassview.as_view(),name='details'),
    path('add/',views.add_data,name='add_data'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
]






