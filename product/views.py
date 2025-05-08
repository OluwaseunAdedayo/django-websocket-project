from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Hello, this is my custom path!")

def home_view(request):
    return HttpResponse("Welcome to the homepage!")

from django.http import JsonResponse
from product.tasks import notify_product_update


def update_product_view(request):
    product_id = 123  # You can later extract this from the request
    notify_product_update.delay(product_id)  # Send task to RabbitMQ via Celery
    return JsonResponse({"status": "Task sent"})

