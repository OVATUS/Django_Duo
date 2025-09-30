from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Table, Reservation
from datetime import datetime
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required

@login_required
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # redirect ไปหน้า login
    else:
        form = SignUpForm()
    return render(request, 'login/signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)  # ❌ ห้ามส่ง request
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user:
                login(request, user)
                return redirect("signup")
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

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



def dashboard_view(request):
    return render(request, 'login/dashboard.html')

