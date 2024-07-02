from django.shortcuts import render

# Create your views here.

# api/views.py

from django.http import JsonResponse
import requests

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def hello_view(request):
    visitor_name = request.GET.get('visitor_name', 'Guest')
    client_ip = get_client_ip(request)

    # Assuming we have a function to get the city from IP (for simplicity, returning a static city)
    city = "New York"

    # Fetch temperature from a weather API
    # Here, we use a mock temperature value; integrate with a real API for production.
    temperature = 11  # degrees Celsius

    response_data = {
        "client_ip": client_ip,
        "location": city,
        "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"
    }

    return JsonResponse(response_data)
