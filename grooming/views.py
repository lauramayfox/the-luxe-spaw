from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

# Home Page
def home(request, template_name="index.html"):
    return render(
        request, template_name
    )

# About Page

def about(request, template_name="about.html"):
    return render(
        request, template_name,
    )

