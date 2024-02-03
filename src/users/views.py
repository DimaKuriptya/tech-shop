from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from carts.models import Cart
from carts.utils import get_user_carts
from .forms import RegistrationForm, LoginForm, UpdateForm
from .models import User
from django.contrib.auth.views import PasswordResetView


def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)

        session_key = request.session.session_key

        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data["email"]
            user.save()
            login(request, user)

            # Transferring anonymous user's cart to the account he registered
            session_carts = Cart.objects.filter(session_key=session_key)
            if session_carts.exists():
                user_carts = get_user_carts(request)
                for cart in session_carts:
                    existed_product = user_carts.filter(product=cart.product)
                    if existed_product.exists():
                        existed_product = existed_product.first()
                        existed_product.quantity += cart.quantity
                        existed_product.save()
                        cart.delete()
                    else:
                        cart.owner = request.user
                        cart.session_key = None
                        cart.save()

            messages.success(request, "Ви успішно створили новий аккаунт")
            return redirect(to="goods:index")
    else:
        form = RegistrationForm()
    context = {"form": form}
    return render(request, "users/registration.html", context)


def login_user(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        session_key = request.session.session_key

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)

            # Transferring anonymous user's cart to the account he logged in
            session_carts = Cart.objects.filter(session_key=session_key)
            if session_carts:
                user_carts = get_user_carts(request)
                for cart in session_carts:
                    existed_product = user_carts.filter(product=cart.product)
                    if existed_product.exists():
                        existed_product = existed_product.first()
                        existed_product.quantity += cart.quantity
                        existed_product.save()
                        cart.delete()
                    else:
                        cart.owner = request.user
                        cart.session_key = None
                        cart.save()

            messages.success(request, "Успішний вхід в аккаунт")
            next_page = request.POST.get("next", None)
            if next_page:
                return redirect(next_page)
            return redirect(to="goods:index")
    else:
        form = LoginForm()
    context = {"form": form}
    return render(request, "users/login.html", context)


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Успішний вихід із аккаунту")
    return redirect(to="goods:index")


@login_required(login_url="users:login")
def profile(request):
    return render(request, "users/profile.html")


@login_required(login_url="users:login")
def edit_profile(request):
    if request.method == "POST":
        form = UpdateForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data["email"]
            user.save()
            messages.success(request, "Успішна зміна даних профілю")
            return redirect("users:profile")
    else:
        form = UpdateForm()

    context = {"form": form}
    return render(request, "users/edit_profile.html", context)
