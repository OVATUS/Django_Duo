
from django.urls import path 
from curd_table.views import *

urlpatterns = [
    path('table/', curd_table_view.as_view(), name='curd_table'),
    path('table/<int:pk>/', Tabledetail.as_view(), name='table_detail'),
    path('table/create/',createtable.as_view(), name='table_create'),
    path('table/update/<int:pk>/', Tableupdate.as_view(), name = 'table_update'),
    path('table/delete/<int:pk>/', TableDelete.as_view(),name = "table_delete"),
]