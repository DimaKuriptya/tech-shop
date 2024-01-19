from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        user = authenticate(
            request,
            username=request.POST.get('username', None),
            password=request.POST.get('password', None),
        )
        if user is not None:
            login(request, user)
            return redirect(to='goods:index')
    form = LoginForm()
    context = {"form": form}
    return render(request, "users/login.html", context)


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(to='goods:index')
