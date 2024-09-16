from django.urls import path 
from . import views
from .views import BookingUpdateView, BookingDeleteView, user_profile


urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.create_booking, name='create_booking'),
    path('profile/', views.user_profile, name='profile'),
    path('confirm_booking/', views.confirm_booking, name='confirm_booking'),
    path('success/', views.booking_success, name='booking_success'),
    path('booking/delete/<int:pk>/', BookingDeleteView.as_view(), name='delete_booking'),
    path('booking/update/<int:pk>/', BookingUpdateView.as_view(), name='update_booking'),

  

]



