from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import BookingForm
from .models import Groomer, Service, Booking
from datetime import datetime, timedelta, time
from django.http import HttpResponse
from django.contrib import messages

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Process the booking request
            booking = form.save(commit=False)
            booking.user = request.user  # Associate the booking with the current user
            booking.save()
            
            # Redirect to the success page
            return redirect('booking/booking_success.html')
    else:
        form = BookingForm()

    return render(request, 'booking/create_booking.html', {'form': form})


def confirm_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    # return redirect('create_booking')
    return redirect('booking_success')


def update_booking(request, id):
    booking = get_object_or_404(Booking, id=id, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = BookingForm(instance=booking)
    
    return render(request, 'update_booking.html', {'form': form})



def delete_booking(request, id):
    booking = get_object_or_404(Booking, id=id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('user_profile')


def index(request):
    """
    Renders Home Page.
    """
    return render(request, "index.html", {})


def booking_success(request):
    """
    View to render the booking success page after a booking request.
    """
    return render(request, 'booking/booking_success.html')

def user_profile(request):
    """
    Renders the user profile page.
    """
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/user_profile.html',)