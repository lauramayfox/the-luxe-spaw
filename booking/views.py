from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages
# Create your views here.

def index(request):
    """
    Renders Home Pg
    """
    return render(request, "index.html",{})


#Booking Form
def booking(request):
    """
    Renders booking page
    """
    return render(request, 'booking.html')
