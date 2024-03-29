from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views


app_name = "users"

urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name='users/password_reset.html',
            success_url=reverse_lazy("users:password_reset_done"),
            email_template_name="users/password_reset_email.html",
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done",
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html',
            success_url=reverse_lazy("users:password_reset_complete")
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done",
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name="password_reset_complete",
    ),
]
