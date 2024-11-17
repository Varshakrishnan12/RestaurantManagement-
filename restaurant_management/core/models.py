from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

from django.db import models


class CustomUser(AbstractUser):

    ROLE_CHOICES = (

        ('admin', 'Admin'),

        ('customer', 'Customer'),

    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


class Restaurant(models.Model):

    name = models.CharField(max_length=100)

    address = models.CharField(max_length=255)

    phone_number = models.CharField(max_length=15)


class MenuItem(models.Model):

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    description = models.TextField()

    available = models.BooleanField(default=True)


class Order(models.Model):

    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    items = models.JSONField()  # Store item ids and quantities

    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(max_length=20, default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)


class Reservation(models.Model):

    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    reservation_time = models.DateTimeField()

    number_of_guests = models.PositiveIntegerField()