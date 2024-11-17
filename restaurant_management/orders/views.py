from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):  # Use ModelViewSet for full CRUD functionality
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

import stripe

from django.conf import settings


stripe.api_key = settings.STRIPE_SECRET_KEY


def create_payment(amount):

    try:

        charge = stripe.Charge.create(

            amount=amount,

            currency='usd',

            description='Order Payment'

        )

        return charge

    except Exception as e:

        # Handle exception

        return None