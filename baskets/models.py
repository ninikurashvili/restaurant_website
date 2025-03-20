from django.db import models

from menu.models import MenuItem
from users.models import CustomUser


# Create your models here.
class Basket(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.item.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.item.name} ({self.quantity})"

