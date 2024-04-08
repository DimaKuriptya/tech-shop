from django.urls import path
from . import viewsets


app_name = 'api_orders'

urlpatterns = [
    path('', viewsets.OrderAPI.as_view()),
]
