from django.urls import path
from . import viewsets


app_name = 'api_goods'

urlpatterns = [
    path('', viewsets.CartAPIList.as_view()),
    path('<int:pk>/', viewsets.CartDetailsAPI.as_view()),
]
