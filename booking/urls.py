from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.create_booking, name='create_booking'),
    path('success/', views.booking_success, name='booking_success'),
    path('my-profile/', views.user_profile, name='profile'),
    # path('edit-booking/', views.edit-booking, name='edit-booking'),
    # path('delete-booking/', views.delete-booking, name='delete-booking'),

]