from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/<slug:slug>/', views.product, name='product')
]