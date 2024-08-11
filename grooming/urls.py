from django.urls import include, path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]