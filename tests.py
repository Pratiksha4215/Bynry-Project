from django.test import TestCase
from django.urls import reverse
from .models import ServiceRequest, Customer

class ServiceRequestModelTestCase(TestCase):
    def test_service_request_creation(self):
        customer = Customer.objects.create(name="Test Customer", email="test@example.com", phone="123456789")
        service_request = ServiceRequest.objects.create(customer=customer, request_type="Test Request", details="Test details")
        self.assertEqual(service_request.customer, customer)
        self.assertEqual(service_request.request_type, "Test Request")
        self.assertEqual(service_request.details, "Test details")

class ServiceRequestViewTestCase(TestCase):
    def test_submit_service_request_view(self):
        url = reverse('submit_service_request')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'submit_service_request.html')

    def test_request_tracking_view(self):
        url = reverse('request_tracking')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'request_tracking.html')
from django.test import TestCase

# Create your tests here.
