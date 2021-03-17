"""Bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from home import views
# from home.views import details,listdetails
from home.views import list_details

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('test',views.employee),
    # path('class/',views.naveen.as_View()),
    # path('view/',MyView.as_view()),
    # path('details/<str:id>',details.as_view()),
    # path('listdetails',listdetails.as_view()),
    path('home',list_details.as_view()),
]
