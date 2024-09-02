from django.shortcuts import render, redirect
from .forms import BookingForm
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, timedelta
from .models import Groomer, Service
from django.contrib import messages
# Create your views here.

def create_booking(request):

    """
    Renders booking page
    """
    return render(request, 'create_booking.html')
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return
            redirect('booking_success') # redirect to a booking success confirmation page/msg
        else:
                form = BookingForm()
                return render(request, 'booking/create_booking.html', {'form': form})



def booking_success(request):
    return render(request, 'booking/booking_success.html')

def index(request):
    """
    Renders Home Pg
    """
    return render(request, "index.html",{})


# #Booking Form
# def booking(request):
#     """
#     Renders booking page
#     """
#     return render(request, 'create_booking.html')


def user_profile(request):

    return render(
                request, 'user-profile.html', )
