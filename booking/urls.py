from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.create_booking, name='create_booking'),
    # path('profile/', views.user_profile, name='user_profile'),
    path('profile/', views.user_profile, name='profile'),
    path('confirm_booking/', views.confirm_booking, name='confirm_booking'),
    path('success/', views.booking_success, name='booking_success'),
    path('booking/update/<int:id>/', views.update_booking, name='update_booking'),
    path('booking/delete/<int:id>/', views.delete_booking, name='delete_booking'),
    

]



