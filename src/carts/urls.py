from django.urls import path
from . import views


app_name = 'carts'

urlpatterns = [
    path('cart_add/<slug:product_slug>/', views.cart_add, name='cart_add'),
]
