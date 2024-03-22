from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL pattern for the index view
    path('service_requests/', views.service_request_list, name='service_request_list'),  # URL pattern for the service request list view
    path('service_requests/<int:pk>/', views.service_request_detail, name='service_request_detail'),  # URL pattern for the service request detail view
    path('request-tracking/', views.request_tracking, name='request_tracking'),
    # Add more URL patterns for other views as needed
]
