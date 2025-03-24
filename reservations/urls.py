from django.urls import path

from .views import check_availability, book_table, view_reservations, cancel_reservation

urlpatterns = [
    path('check-availability/', check_availability, name='check_availability'),
    path('book-table/<int:table_id>/<str:date>/<str:time>/<int:people>/', book_table, name='book_table'),
    path('my-reservations/', view_reservations, name='view_reservations'),
    path('cancel-reservation/<int:reservation_id>/', cancel_reservation, name='cancel_reservation'),

]