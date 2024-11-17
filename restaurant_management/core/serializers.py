from rest_framework import serializers
from .models import Restaurant, MenuItem

# Serializer for Restaurant
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'phone_number']

# Serializer for MenuItem
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'restaurant', 'name', 'price', 'description', 'available']
