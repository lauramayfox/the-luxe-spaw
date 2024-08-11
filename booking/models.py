from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

GROOMING_CHOICES = (
    ("X-Large Size Grooming", "X-Large Size Grooming"),
    ("Large Size Grooming", "Large Size Grooming"),
    ("Medium Size Grooming", "Medium Size Grooming"),
    ("Bath + Blowdry (X-Large)", "Bath + Blowdry (X-Large)"),
    ("Bath + Blowdry (Large)", "Bath + Blowdry (Large)"),
    ("Bath + Blowdry (Medium)", "Bath + Blowdry (Medium)"),
    ("Bath + Blowdry (Small)", "Bath + Blowdry (Small)"),
    ("Nails/Ears", "Nails/Ears"),
    ("Teeth", "Teeth"),
    )


CONFIRMATION = (
    ('Awaiting confirmation', 'Awaiting confirmation'),
    ('Booking confirmed', 'Booking confirmed'), 
    ('Booking declined', 'Booking declined'),
    )

TIME_CHOICES = (
    ("10 AM", "10 AM"),
    ("11 AM", "11 AM"),
    ("12 PM", "12 PM"),   #Lunch 1-2pm, no booking
    ("2 PM", "2 PM"),
    ("3 PM", "3 PM"),
    ("4 PM", "4 PM"),
    ("5 PM", "5 PM"),
    ("7 PM", "7 PM"),
)

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(null=True, max_length=50)
    last_name = models.CharField(null=True, max_length=50)
    email = models.EmailField(max_length=300)

    def __str__(self):
        if self.user:
            return self.email


# Booking
class Booking(models.Model):

    booking_customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    booking_date = models.DateField(default=datetime.date)
    booking_time = models.CharField(choices=TIME_CHOICES, default='10 AM', max_length=50)
    booked_on = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.CharField(choices=CONFIRMATION, default='Awaiting confirmation', max_length=50)