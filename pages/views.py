from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contacts
from .forms import Contact_form
from django.core.mail import send_mail

# Create your views here.

def home(request):
    context = {
    "ptitle": "|Home",
        }
    return render(request, "pages/index.html", context )

def projects(request):
    context = {
        "ptitle": "|My Projects",
        }
    return render(request, "pages/projects.html", context)

def contact(request):
    context = {
        "form":Contact_form,
        "message" : "I'd love to hear from you!",
        "ptitle": "|Contact Us!"
    }
    return render(request, "pages/contact.html", context)

def contact_form(request):
    if request.method == "POST":
        form = Contact_form(request.POST)
        if form.is_valid():
            form_name = form.cleaned_data["name"]
            form_email = form.cleaned_data["email"]

            form_number = form.cleaned_data["number"]
            subject = "[Portfolio]" + form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            contact = Contacts(name = form_name, email = form_email,number =  form_number)
            contact.save()

            #send_mail(
            #   subject,
            #   message,
            #    "y.yayaoye@gmail.com",
            #    {form_email},
            #    fail_silently=False,
            #   ) 

    context = {
        "form":Contact_form,
        "message" : "Thank you for submitting, we'll be in touch soon!",
    }
    return render(request, "pages/contact.html", context)