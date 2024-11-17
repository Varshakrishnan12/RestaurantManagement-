from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet  # Note the updated viewset class

# Create a router instance
router = DefaultRouter()
router.register(r'orders', OrderViewSet)  # Register the OrderViewSet

urlpatterns = [
    path('', include(router.urls)),  # Automatically includes 'orders/' route
]
