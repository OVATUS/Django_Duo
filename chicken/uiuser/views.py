from urllib import request
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Table, Reservation
from datetime import datetime, timedelta
import json


def table_plan(request, restaurant_id):
    today = timezone.localdate()
    start_of_day = datetime.combine(today, datetime.min.time(), tzinfo=timezone.get_current_timezone())
    end_of_day = datetime.combine(today, datetime.max.time(), tzinfo=timezone.get_current_timezone())

    tables = Table.objects.filter(restaurant_id=restaurant_id)
    today_reservations = Reservation.objects.filter(
        table__restaurant_id=restaurant_id,
        reservation_time__range=(start_of_day, end_of_day),
        status="confirmed"
    )
    booked_table_ids = today_reservations.values_list("table_id", flat=True)

    if request.method == "POST":
        table_ids = json.loads(request.POST.get("table_ids", "[]"))
        reservation_time = request.POST.get("reservation_time")

        for table_id in table_ids:
            Reservation.objects.create(
                user=request.user,
                table_id=table_id,
                reservation_time=reservation_time,
                status="confirmed"
            )
        return redirect("reservation_success")

    return render(request, "reservations/table_plan.html", {
        "tables": tables,
        "booked_table_ids": booked_table_ids,
        "today": today
    })



def reservation_success(request):
    return render(request, "reservations/success.html")
