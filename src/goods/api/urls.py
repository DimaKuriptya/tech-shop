from django.urls import path
from . import viewsets

app_name = 'api'

urlpatterns = [
    path('categories/', viewsets.CategoryAPIView.as_view()),
    path('goods/', viewsets.ProductAPIView.as_view()),
]
