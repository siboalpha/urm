from .models import *
from django.forms import ModelForm, TextInput, Textarea, EmailInput

class ContactForm(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'message']

        widgets = {
            'first_name': TextInput(attrs={'class': ' form-control', 'placeholder': 'Your first name'}),
            'last_name': TextInput(attrs={'class': ' form-control', 'placeholder': 'Your last name'}),
            'email': EmailInput(attrs={'class': ' form-control', 'placeholder': 'Your email address'}),
            'phone_number': TextInput(attrs={'class': ' form-control', 'placeholder': 'Your phone number'}),
            'message': Textarea(attrs={'class': ' form-control', 'placeholder': 'Your message'}),
        }

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'location']

        widgets = {
            'first_name': TextInput(attrs={'class': ' form-control', 'placeholder': 'Your first name'}),
            'last_name': TextInput(attrs={'class': ' form-control', 'placeholder': 'Your last name'}),
            'email': EmailInput(attrs={'class': ' form-control', 'placeholder': 'Your email address'}),
            'phone_number': TextInput(attrs={'class': ' form-control', 'placeholder': 'Your phone number'}),
            'location': TextInput(attrs={'class': ' form-control', 'placeholder': 'Your location'}),
        }