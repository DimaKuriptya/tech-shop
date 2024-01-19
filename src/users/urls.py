from django.urls import path
from .views import login_user, logout_user, register_user, profile


app_name = 'users'

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile')
]
