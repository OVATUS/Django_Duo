<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Table, Reservation
from datetime import datetime
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm
=======
from urllib import request
from django.utils import timezone
from .models import Table, Reservation
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm
>>>>>>> 2b6a10c (ทำหน้เา html ทั้งหมด)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # redirect ไปหน้า dashboard
    else:
        form = SignUpForm()
    return render(request, 'login/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

<<<<<<< HEAD
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


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "สมัครสมาชิกเรียบร้อยแล้ว! กรุณาล็อกอิน")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("reservation_history")  # หลังล็อกอินไปหน้า history
            else:
                messages.error(request, "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")
=======
def dashboard_view(request):
    return render(request, 'login/dashboard.html')
>>>>>>> 2b6a10c (ทำหน้เา html ทั้งหมด)
