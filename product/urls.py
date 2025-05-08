# product/urls.py
from django.urls import path
from .views import update_product_view

urlpatterns = [
    path('update-product/', update_product_view, name='update_product'),
]
