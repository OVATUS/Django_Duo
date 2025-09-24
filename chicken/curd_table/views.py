from django.shortcuts import render
from django.views.generic import TemplateView , ListView , CreateView , UpdateView , DeleteView, DetailView
from .models import Table

class curd_table_view(ListView):
    template_name = 'Apptable/table_list.html'
    model = Table
    context_object_name = 'tables'
    queryset = Table.objects.all()
