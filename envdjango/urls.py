# envdjango/urls.py
from django.contrib import admin
from django.urls import path, include
from product.routes.test import test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),  # <-- This includes routes from product
    path('test/',test.as_view(),name="test")
]
