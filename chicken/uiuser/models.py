from django.db import models
from django.contrib.auth.models import AbstractUser

# ---- User ----
class User(AbstractUser):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"


# ---- Table ----
class Table(models.Model):
    zone = models.CharField(max_length=50)
    table_number = models.CharField(max_length=10, unique=True)  # ไม่ให้ซ้ำ
    seats = models.IntegerField(default=4)

    # พิกัดแผนผังโต๊ะ (optional)
    pos_x = models.IntegerField(default=0)
    pos_y = models.IntegerField(default=0)

    def __str__(self):
        return f"Table {self.table_number} (Zone {self.zone}, Seats {self.seats})"


# ---- Reservation ----
class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="reservations")
    reservation_time = models.DateTimeField()
    end_time = models.DateTimeField()   # เวลาเลิก
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation by {self.user.username} on {self.reservation_time} - {self.status}"