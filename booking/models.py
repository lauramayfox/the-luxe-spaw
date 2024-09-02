from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Groomer(models.Model):
    name = models.CharField(max_length=200)
    experience_level = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6,
    decimal_places=2)
    groomers = models.ManyToManyField(Groomer, related_name='services')

    def __str__(self):
        return self.name




class Booking(models.Model):
    service = models.ForeignKey(Service,
    on_delete=models.CASCADE)
    groomer = models.ForeignKey(Groomer, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 
        f"Booking for {self.customer_name} on {self.date_time.strftime('%Y-%m-%d%H:%M')}"

# GROOMING_CHOICES = (
#     ("X-Large Size Grooming", "X-Large Size Grooming"),
#     ("Large Size Grooming", "Large Size Grooming"),
#     ("Medium Size Grooming", "Medium Size Grooming"),
#     ("Bath + Blowdry (X-Large)", "Bath + Blowdry (X-Large)"),
#     ("Bath + Blowdry (Large)", "Bath + Blowdry (Large)"),
#     ("Bath + Blowdry (Medium)", "Bath + Blowdry (Medium)"),
#     ("Bath + Blowdry (Small)", "Bath + Blowdry (Small)"),
#     ("Nails/Ears", "Nails/Ears"),
#     ("Teeth", "Teeth"),
#     )

# TIME_CHOICES = (
#     ("10 AM", "10 AM"),
#     ("11 AM", "11 AM"),
#     ("12 PM", "12 PM"),   #Lunch 1-2pm, no booking
#     ("2 PM", "2 PM"),
#     ("3 PM", "3 PM"),
#     ("4 PM", "4 PM"),
#     ("5 PM", "5 PM"),
#     ("7 PM", "7 PM"),
# )

