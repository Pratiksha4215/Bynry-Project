# customer_service/views.py

from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest

def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer
            service_request.status = "Pending"  # Set initial status
            service_request.save()
            return redirect('request_tracking')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_service_request.html', {'form': form})

def request_tracking(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'request_tracking.html', {'service_requests': service_requests})
from django.shortcuts import render
def request_tracking(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'request_tracking.html', {'service_requests': service_requests})


# Create your views here.
