from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from baskets.models import Basket
from .models import Order, OrderItem


@login_required
def place_order(request):
    basket_items = Basket.objects.filter(user=request.user)
    if not basket_items:
        return redirect('view_basket')
    total_price = sum(item.total_price for item in basket_items)

    order = Order.objects.create(
        user=request.user,
        status='Pending',
        total_price=total_price
    )
    for item in basket_items:
        OrderItem.objects.create(
            order=order,
            item=item.item,
            quantity=item.quantity,
            price=item.item.price
        )
        item.delete()
    return redirect('order_success')
@login_required
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.status='Canceled'
    order.save()
    return redirect('view_order')

@login_required
def view_order(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    context = {
        "orders": orders,
    }
    return render(request, "order_history.html", context)

@login_required
def view_order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = OrderItem.objects.filter(order=order)

    context = {
        "order": order,
        "order_items": order_items,
    }
    return render(request, "order_details.html", context)

@login_required
def order_success(request):
    return render(request, "order_success.html")