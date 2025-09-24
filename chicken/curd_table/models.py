from django.db import models

class Table(models.Model):
    table_number = models.CharField(max_length=10, unique=True)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)
    location = models.CharField(max_length=20, choices=(('indoor','Indoor'), ('outdoor','Outdoor')))
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Table {self.table_number} ({self.capacity} seats)"