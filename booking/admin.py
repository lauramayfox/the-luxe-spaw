from django.contrib import admin
from .models import Service, Groomer, Booking
# Register your models here.

admin.site.register(Service)
admin.site.register(Groomer)
admin.site.register(Booking)