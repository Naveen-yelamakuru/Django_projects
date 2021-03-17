from django.urls import path
from . import views
from home.models import Provider



urlpatterns = [
    path('api',views.homegenerics.as_view()),
]