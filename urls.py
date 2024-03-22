from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customer_service.urls')),  # Include the URL configuration for the customer_service app
    # Add more URL patterns for other apps as needed
]


