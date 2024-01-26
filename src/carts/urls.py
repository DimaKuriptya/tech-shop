from django.urls import path
from . import views


app_name = 'carts'

urlpatterns = [
    path('cart-add/', views.cart_add, name='cart_add'),
    path('cart-delete/', views.cart_delete, name='cart_delete'),
    path('cart-change/', views.cart_change, name='cart_change'),
]
