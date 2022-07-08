from email import message
from http import client
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from django.core.mail import EmailMessage
from core import settings
from django.template.loader import render_to_string

from .forms import *
# Create your views here.

def index(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("message has been saved")
    context = {'form': form}
    return render(request, 'index.html', context)

def shop(request):
    return render(request, 'shop.html')

def bag(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.bag = "Default bag"
            form.save()

            client_name = form.cleaned_data['first_name']
            client_email = form.cleaned_data['email']
            client_location = form.cleaned_data['location']
            client_order = "Example Order"
            context = {'client_name': client_name, 'client_email': client_email, 'client_order': client_order, 'client_location': client_location}
            email_template = render_to_string('emails/new_order.html', context)

            email = EmailMessage(
                "New Order",
                email_template,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER]
            )
            email.fail_silently = False
            try:
                email.send()
            except:
                return HttpResponse("Order received but we did not get a notification")
            return HttpResponse("it's working")
    context = {'form': form}
    return render(request, 'bag.html', context)

