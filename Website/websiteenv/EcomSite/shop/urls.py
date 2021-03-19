from django.urls import path,include
from shop import views

urlpatterns = [
    path('checkout/',views.checkout,name='checkour'),
]