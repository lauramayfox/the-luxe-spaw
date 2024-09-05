from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import BookingForm
from .models import Groomer, Service
from datetime import datetime, timedelta, time

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()

    # Define available times based on business hours
    available_times = [
        "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00",  # Weekday hours
        "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"  # Saturday hours
    ]

    return render(request, 'create_booking.html', {'form': form, 'available_times': available_times})


def booking_success(request):
    """
    Renders a booking success confirmation page.
    """
    return render(request, 'booking_success.html')

def index(request):
    """
    Renders Home Page.
    """
    return render(request, "index.html", {})

def user_profile(request):
    """
    Renders the user profile page.
    """
    return render(request, 'user-profile.html')

