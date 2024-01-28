from django.urls import path
from .views import ipn

urlpatterns = [
    path('ipn/', ipn, name='paypal-ipn'),
]
