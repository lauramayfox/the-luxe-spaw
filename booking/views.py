from django.shortcuts import get_object_or_404,render, redirect
from django.http import JsonResponse
from .forms import BookingForm
from .models import Groomer, Service, Booking
from datetime import datetime, timedelta, time
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Process the booking request
            booking = form.save(commit=False)
            booking.user = request.user  # Associate the booking with the current user
            booking.save()
            
            # Redirect to the success page
            return redirect('booking_success')

    else:
        form = BookingForm()

    return render(request, 'booking/create_booking.html', {'form': form})



def confirm_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)  
            booking.user = request.user  # logged-in user
            booking.save()  
            return redirect('booking_success')
    return redirect('create_booking')







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


@login_required
def user_profile(request):
    bookings = Booking.objects.filter(user=request.user)  # Ensure request.user is properly referenced
    return render(request, 'booking/user_profile.html', {'bookings': bookings})



class BookingUpdateView(UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/update_booking.html'


class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'booking/delete_booking.html'

    def get_success_url(self):
        return redirect('user_profile')