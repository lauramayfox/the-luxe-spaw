from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import BookingForm
from .models import Groomer, Service
from datetime import datetime, timedelta, time
from django.http import HttpResponse
from django.contrib import messages

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or similar
    else:
        form = BookingForm()

    return render(request, 'create_booking.html', {'form': form})



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

