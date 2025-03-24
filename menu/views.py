from django.shortcuts import render, redirect, get_object_or_404
from baskets.models import Basket
from .models import MenuItem, Category
from django.contrib.auth.decorators import login_required

def all_menu_items(request):
    menu_items = MenuItem.objects.all()
    context = {"menu_items": menu_items}
    return render(request, "menuitems.html", context)

def menu_search(request):
    query = request.GET.get("search", "")
    selected_category = request.GET.get("category", "")
    menu_items = MenuItem.objects.all()
    if query:
        menu_items = menu_items.filter(name__icontains=query)
    if selected_category:
        menu_items = menu_items.filter(category_id=selected_category)
    categories = Category.objects.all()
    context = {
        "menu_items": menu_items,
        "query": query,
        "categories": categories,
        "selected_category": selected_category,
    }
    return render(request, "menuitems.html", context)

@login_required(login_url='login')
def add_to_basket(request, item_id):
    menu_item = get_object_or_404(MenuItem, id=item_id)
    basket_item, created = Basket.objects.get_or_create(user=request.user, item=menu_item)
    if not created:
        basket_item.quantity += 1
        basket_item.save()
    else:
        basket_item.quantity = 1
        basket_item.save()
    return redirect('all_menu_items')