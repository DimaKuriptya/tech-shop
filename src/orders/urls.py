from django.urls import path
from . import views


app_name = 'orders'

urlpatterns = [
    path('create_order/', views.create_order, name='create_order'),
    path('payment_success/<int:order_id>/', views.payment_success, name='payment_success'),
    path('payment_fail/<int:order_id>/', views.payment_fail, name='payment_fail'),
]
