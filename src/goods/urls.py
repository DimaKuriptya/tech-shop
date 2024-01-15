from django.urls import path
from . import views

app_name = 'goods'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:cat_slug>/', views.view_category, name='view_category'),
    path('product/<slug:slug>/', views.product, name='product')
]
