from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Groomer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,
    decimal_places=2)
    groomers = models.ManyToManyField(Groomer, related_name='services')

    def __str__(self):
        return self.name



class Booking(models.Model):
    service = models.ForeignKey(Service,
    on_delete=models.CASCADE)
    groomer = models.ForeignKey(Groomer, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    booking_date = models.DateField()
    booking_time = models.TimeField()

    def __str__(self):
        return 
        f"Booking for {self.customer_name} on {self.date_time.strftime('%Y-%m-%d%H:%M')}"

    booking_datetime = models.DateTimeField()




