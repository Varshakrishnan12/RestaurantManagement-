from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):

    ROLE_CHOICES = (

        ('admin', 'Admin'),

        ('customer', 'Customer'),

    )
    # Add related_name to avoid clash
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='orders_user_set',  # Ensure this is unique across all CustomUser models
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='orders_user_permissions_set',  # Ensure this is unique across all CustomUser models
        blank=True
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


class Restaurant(models.Model):

    name = models.CharField(max_length=100)

    address = models.CharField(max_length=255)

    phone_number = models.CharField(max_length=15)

class Order(models.Model):

    objects = None
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    items = models.JSONField()  # Store item ids and quantities

    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(max_length=20, default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)