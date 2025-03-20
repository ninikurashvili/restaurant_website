from django.urls import path
from .views import all_menu_items, add_to_basket, menu_search

urlpatterns = [
    path('menu/', all_menu_items, name='all_menu_items'),
    path("menu/search/", menu_search, name="menu_search"),
    path('add_to_basket/<int:item_id>/', add_to_basket, name='add_to_basket'),
]