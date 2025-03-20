from django.shortcuts import render, redirect, get_object_or_404
from .models import Basket
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def view_basket(request):
    basket_items = Basket.objects.filter(user=request.user)
    total_order_price = sum(item.total_price for item in basket_items)
    return render(request, 'basketitems.html', {
        'basket_items': basket_items,
        'total_order_price': total_order_price
    })

@login_required
def increase_quantity(request, item_id):
    basket_item = get_object_or_404(Basket, id=item_id, user=request.user)
    basket_item.quantity += 1
    basket_item.save()
    return redirect('view_basket')

@login_required
def decrease_quantity(request, item_id):
    basket_item = get_object_or_404(Basket, id=item_id, user=request.user)
    if basket_item.quantity > 1:
        basket_item.quantity -= 1
        basket_item.save()
    return redirect('view_basket')

@login_required
def remove_from_basket(request, item_id):
    basket_item = get_object_or_404(Basket, id=item_id, user=request.user)
    basket_item.delete()
    return redirect('view_basket')


