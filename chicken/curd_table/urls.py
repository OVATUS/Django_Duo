
from django.urls import path 
from curd_table import views

urlpatterns = [
    path('curd_table/', views.curd_table, name='curd_table'),
]