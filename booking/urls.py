from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.booking, name='booking'),
    # name='preview_booking'),
    # path('user-profile/', views.user-profile, name='user-profile'),
    # path('edit-booking/', views.edit-booking, name='edit-booking'),
    # path('delete-booking/', views.delete-booking, name='delete-booking'),

]