from django.db import models

# Create your models here.

class ContactFormMessage(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255)
    message = models.TextField(max_length=2555)


class Order(models.Model):
    bag = models.CharField(max_length=2550)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255)
    location = models.CharField(max_length=2550)
