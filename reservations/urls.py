from django.urls import path

from .views import check_availability, book_table, view_reservations

urlpatterns = [
    path('check-availability/', check_availability, name='check_availability'),
    path('book-table/<int:table_id>/<str:date>/<str:time>/<int:people>/', book_table, name='book_table'),
    path('my-reservations/', view_reservations, name='view_reservations'),
]