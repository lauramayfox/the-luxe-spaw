from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dog_grooming(request):
    return HttpResponse("greetings, dogs!")