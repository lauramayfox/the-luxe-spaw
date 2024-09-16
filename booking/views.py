from django.shortcuts import get_object_or_404,render, redirect
from .forms import BookingForm
from .models import Groomer, Service, Booking
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

def create_booking(request):
    """
    Process booking request
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            
            return redirect('booking_success')

    else:
        form = BookingForm()

    return render(request, 'booking/create_booking.html', {'form': form})



def confirm_booking(request):
    """
    Confirm Booking & redirect to success pg
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)  
            booking.user = request.user
            booking.save()  
            return redirect('booking_success')
    return redirect('create_booking')


def update_booking(request, id):
    """
    Updates a currently booked appointment
    """
    booking = get_object_or_404(Booking, id=id)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'booking/create_booking.html', {'form': form})


class BookingUpdateView(UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/create_booking.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return get_object_or_404(Booking, pk=self.kwargs['pk'])

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BookingDeleteView(DeleteView):
    model = Booking
    success_url = reverse_lazy('profile')
    template_name = 'booking/delete_booking.html'


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
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/user_profile.html', {'bookings': bookings})


