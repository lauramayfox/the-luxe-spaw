from django.shortcuts import render


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