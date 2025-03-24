from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from reservations.models import Reservation, Table

@login_required(login_url='login')
def check_availability(request):
    all_tables = Table.objects.all()
    current_time = datetime.now()
    today = current_time.date()
    if request.method == 'POST':
        date_str = request.POST.get('date')
        time_str = request.POST.get('time')
        people_str = request.POST.get('people')
        errors = {}
        try:
            selected_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            selected_time = datetime.strptime(time_str, "%H:%M").time()
            now_time = datetime.now().replace(microsecond=0).time()
            if selected_date < today:
                errors['error_date'] = "You cannot select a past date."
            elif selected_time < now_time and selected_date == today:
                errors['error_time'] = "You cannot select a past time today."
            people = int(people_str)
            if people <= 0:
                errors['error_people'] = "Invalid number of people."
        except ValueError:
            errors['error_date'] = "Invalid date format."
        if errors:
            return render(request, 'reservation.html', {
                **errors,
                'all_tables': all_tables,
                'available_table_ids': [],
                'today': today,
                'date': date_str,
                'time': time_str,
                'people': people_str
            })
        time_before = (datetime.combine(selected_date, selected_time) - timedelta(hours=2)).time()
        time_after = (datetime.combine(selected_date, selected_time) + timedelta(hours=2)).time()
        booked_tables = Reservation.objects.filter(
            date=selected_date,
            time__range=(time_before, time_after)
        ).values_list('table_id', flat=True)

        available_tables = Table.objects.exclude(id__in=booked_tables).filter(seats__gte=people)

        return render(request, 'reservation.html', {
            'all_tables': all_tables,
            'available_table_ids': [table.id for table in available_tables],
            'date': date_str,
            'time': time_str,
            'people': people_str,
            'today': today
        })

    return render(request, 'reservation.html', {
        'all_tables': all_tables,
        'available_table_ids': [],
        'today': today
    })

@login_required
def book_table(request, table_id, date, time, people):
    table = get_object_or_404(Table, id=table_id)
    selected_date = datetime.strptime(date, "%Y-%m-%d").date()
    selected_time = datetime.strptime(time, "%H:%M").time()

    time_before = (datetime.combine(selected_date, selected_time) - timedelta(hours=2)).time()
    time_after = (datetime.combine(selected_date, selected_time) + timedelta(hours=2)).time()

    if Reservation.objects.filter(date=date, time__range=(time_before, time_after), table=table).exists():
        return redirect('check_availability')

    Reservation.objects.create(user=request.user, table=table, date=date, time=time, people_number=people)
    return redirect('view_reservations')

@login_required
def view_reservations(request):
    reservations = Reservation.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_reservation.html', {'reservations': reservations})

def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if reservation.date < datetime.now().date():  # Only compares the date (ignoring time)
        messages.error(request, "You cannot cancel a past reservation.")
        return redirect('view_reservations')
    reservation.delete()
    messages.success(request, "Your reservation has been canceled successfully.")
    return redirect('view_reservations')