from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import OrderForm


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.buyer = request.user
            order.save()
            messages.success(request, 'Замовлення успішно оформлено')
            return redirect('users:profile')
    else:
        if request.user.is_authenticated:
            user_details = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'phone_number': request.user.phone_number,
                'email': request.user.email
            }
            form = OrderForm(initial=user_details)
        else:
            form = OrderForm()
    context = {
        'form': form
    }
    return render(request, 'orders/order_creation.html', context)
