from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.booking, name='booking'),
    path('my-profile/', views.user_profile, name='profile'),
    # path('edit-booking/', views.edit-booking, name='edit-booking'),
    # path('delete-booking/', views.delete-booking, name='delete-booking'),

]