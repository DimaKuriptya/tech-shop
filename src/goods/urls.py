from django.urls import path, include
from . import views

app_name = 'goods'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:cat_slug>/', views.index, name='view_category'),
    path('product/<slug:slug>/', views.product_details, name='product_details'),
]
