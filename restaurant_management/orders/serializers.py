from rest_framework import serializers
from .models import  Order

# Serializer for Order
class OrderSerializer(serializers.ModelSerializer):
    # You can define nested serializers for related fields
    customer = serializers.StringRelatedField()  # Or you can use CustomerSerializer if you have one
    # Serialize related Restaurant model
    # For the items field, since it's JSON, you can use a simple serializer or handle it as is
    items = serializers.JSONField()

    class Meta:
        model = Order
        fields = ['id', 'customer', 'restaurant', 'items', 'total_price', 'status', 'created_at']
