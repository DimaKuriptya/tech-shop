from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to="goods:index")
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)


def login_user(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
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
    else:
        form = LoginForm()
    context = {"form": form}
    return render(request, "users/login.html", context)


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(to='goods:index')


def profile(request):
    return render(request, 'users/profile.html')
