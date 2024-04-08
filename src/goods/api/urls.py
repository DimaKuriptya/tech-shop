from django.urls import path
from . import viewsets


app_name = 'api_goods'

urlpatterns = [
    path('categories/', viewsets.CategoryAPIList.as_view()),
    path('goods/', viewsets.ProductAPIList.as_view()),
    path('product/<int:pk>/', viewsets.ProductAPIDetail.as_view()),
]
