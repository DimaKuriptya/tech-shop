from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import RegisterForm, LoginForm


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create(
                username=username,
                password=password
            )
            login(request, user)
            return redirect(to="goods:index")
    form = RegisterForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user:
            login(request, user)
            return redirect(to='goods:index')
    form = LoginForm()
    context = {"form": form}
    return render(request, "users/login.html", context)


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(to='goods:index')


def profile(request):
    return render(request, 'users/profile.html')
