from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

# Create your models here

class Groomer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    groomers = models.ManyToManyField(Groomer, related_name='services')

    def __str__(self):
        return self.name

class Booking(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    groomer = models.ForeignKey(Groomer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    customer_name = models.CharField(max_length=100)
    booking_date = models.DateField()
    booking_time = models.TimeField()

    def __str__(self):
        return f"Booking by {self.user} for {self.service} on {self.booking_date} at {self.booking_time}"


