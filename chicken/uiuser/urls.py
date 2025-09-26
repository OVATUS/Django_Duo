from django.urls import path
from . import views

urlpatterns = [
    path("restaurant/<int:restaurant_id>/tables/", views.table_plan, name="table_plan"),
    path("reservation/success/", views.reservation_success, name="reservation_success"),
]
