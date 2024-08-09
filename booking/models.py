from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

GROOMING_CHOICES = (
    ("Large Size Grooming", "Large Size Grooming"),
    ("Medium Size Grooming", "Medium Size Grooming"),
    ("Small Size Grooming", "Small Size Grooming"),
    ("Bath + Blowdry (Under 25 lbs)", "Bath + Blowdry (Under 25 lbs)"),
    ("Bath + Blowdry (Over 25 lbs)", "Bath + Blowdry (Over 25 lbs)"),
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

DAYS = ((0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'),
        (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday'),)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=GROOMING_CHOICES, default="Grooming Service")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="10 AM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"