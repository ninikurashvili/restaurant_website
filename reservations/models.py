from django.db import models

from users.models import CustomUser


# Create your models here.
class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.PositiveIntegerField()

    def __str__(self):
        return f"Table {self.number} ({self.seats} seats)"

class Reservation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    people_number = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation {self.id} for {self.user.username} on {self.date} at {self.time}"
