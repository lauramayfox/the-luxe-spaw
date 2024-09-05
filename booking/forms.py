
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Booking, Groomer, Service
from datetime import datetime, time, timedelta

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'groomer', 'customer_name', 'booking_date', 'booking_time']  # Use booking_date and booking_time separately
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),  # Use date input widget
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)

        # Populate the service field with all available services
        self.fields['service'].queryset = Service.objects.all()

        # Populate the groomer field with all available groomers
        self.fields['groomer'].queryset = Groomer.objects.all()

        # Set attributes for booking_date field safely inside the __init__ method
        self.fields['booking_date'].widget.attrs.update({
            'min': self.get_min_date()
        })

    def get_min_date(self):
        # Return the minimum date for the booking
        now = datetime.now()
        if now.weekday() == 6:  # If today is Sunday
            now += timedelta(days=1)  # Shift to Monday
        return now.strftime('%Y-%m-%d')  # Format for date input