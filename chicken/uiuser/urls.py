from django.urls import path
from .views import *

urlpatterns = [
<<<<<<< HEAD
    path("restaurant/<int:restaurant_id>/tables/", views.table_plan, name="table_plan"),
    path("reservation/success/", views.reservation_success, name="reservation_success"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
=======
    # User Authentication URLs
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
>>>>>>> 2b6a10c (ทำหน้เา html ทั้งหมด)
]
