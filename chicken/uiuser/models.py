from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True, null=True)

class Table(models.Model):
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE, related_name="tables")
    zone = models.CharField(max_length=50)
    table_number = models.CharField(max_length=10)
    seats = models.IntegerField(default=4)

    # พิกัดแผนผัง
    pos_x = models.IntegerField(default=0)
    pos_y = models.IntegerField(default=0)

    def __str__(self):
        return f"โต๊ะ {self.table_number} (โซน {self.zone})"


class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="reservations")
    reservation_time = models.DateTimeField()
    end_time = models.DateTimeField()   # ✅ เพิ่มช่วงเวลา
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
