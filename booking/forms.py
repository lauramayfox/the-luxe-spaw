
from django import forms
from .models import Booking, Groomer, Service
from datetime import datetime

class BookingForm(forms.ModelForm):
    booking_time = forms.ChoiceField(choices=[], required=True)

    class Meta:
        model = Booking
        fields = ['service', 'groomer', 'booking_date', 'booking_time']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)

        # Populate service and groomer fields
        self.fields['service'].queryset = Service.objects.all()
        self.fields['groomer'].queryset = Groomer.objects.all()

        # Optionally set minimum date for booking
        self.fields['booking_date'].widget.attrs.update({'min': self.get_min_date()})

        # Set time choices
        if 'booking_date' in self.data:
            selected_date = self.data.get('booking_date')
            self.fields['booking_time'].choices = self.get_time_choices(selected_date)
        else:
            self.fields['booking_time'].choices = self.get_time_choices()

    def get_time_choices(self, selected_date=None):
        # Default time slots from 09:00 to 18:00
        return [(f'{hour:02}:00', f'{hour:02}:00') for hour in range(9, 18)]

    def get_min_date(self):
        return datetime.now().strftime('%Y-%m-%d')
