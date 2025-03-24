from django.urls import path

from .views import view_order_details, order_success, place_order, view_order, cancel_order

urlpatterns = [
    path("orders/history/", view_order, name="view_order"),
    path("orders/<int:order_id>/", view_order_details, name="view_order_details"),
    path("order/success/", order_success, name="order_success"),
    path('place_order/', place_order, name='place_order'),
    path('order/cancel/<int:order_id>/', cancel_order, name='cancel_order'),

]