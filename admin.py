# customer_service/admin.py

from django.contrib import admin
from .models import ServiceRequest, Customer

admin.site.register(ServiceRequest)
admin.site.register(Customer)
from django.contrib import admin

# Register your models here.
