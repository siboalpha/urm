from email import message
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

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
            return HttpResponse("it's working")
    context = {'form': form}
    return render(request, 'bag.html', context)

