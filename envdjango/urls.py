# envdjango/urls.py
from django.contrib import admin
from django.urls import path, include
from product.routes.test import test
from product.routes.ask_gilbert import ask_gilbert

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),  
    path('test/',test.as_view(),name="test"),
    path('ask-gilbert/',ask_gilbert.as_view(),name="ask-gilbert")

]
