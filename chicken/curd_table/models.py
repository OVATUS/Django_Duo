from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    category = models.CharField(max_length=50, blank=True, null=True)  # เช่น อาหาร/เครื่องดื่ม

    def __str__(self):
        return self.name