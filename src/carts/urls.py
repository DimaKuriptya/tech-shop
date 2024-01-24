from django.urls import path
from . import views


app_name = 'carts'

urlpatterns = [
    path('cart-add/<slug:product_slug>/', views.cart_add, name='cart_add'),
    path('cart-delete/<slug:product_slug>/', views.cart_delete, name='cart_delete')
]
