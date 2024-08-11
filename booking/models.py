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

