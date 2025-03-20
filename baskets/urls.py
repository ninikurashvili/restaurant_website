from django.urls import path
from .views import view_basket, increase_quantity, remove_from_basket, decrease_quantity

urlpatterns = [
    path('basket/', view_basket, name='view_basket'),
    path('basket/increase/<int:item_id>/', increase_quantity, name='increase_quantity'),
    path('basket/decrease/<int:item_id>/', decrease_quantity, name='decrease_quantity'),
    path('basket/remove/<int:item_id>/', remove_from_basket, name='remove_from_basket'),
]