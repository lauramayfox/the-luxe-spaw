from .models import Booking, UserProfile, GROOMING_CHOICES, TIME_CHOICES
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, TextInput, NumberInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

