from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

# Home Page
def home(request, template_name="index.html"):
    return render(
        request, template_name
    )

# Services Page

def services(request, template_name="services.html"):
    return render(
        request, template_name,
    )

    # Contact Page

def contact(request, template_name="contact.html"):
    return render(
        request, template_name,
    )

