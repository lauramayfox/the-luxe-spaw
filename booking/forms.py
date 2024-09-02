
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'groomer', 'customer_name', 'date_time']
        widgets = {
            'date_time':
            forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

        def __init__(self, *args, **kwargs):
            super(BookingForm, self).__init__(*args, **kwargs)
            if 'service' in self.data:
                try:
                    service_id = int(self.data.get('service')) 
                    self.fields['groomer'].queryset = Groomer.objects.filter(services__id=service_id)
                
                except (ValueError, TypeError):
                    pass #ignore invalid input
                else: 
                    self.fields['groomer'].queryset = Groomer.objects.none() # No Groomer available