from django.shortcuts import render
from django.views.generic import TemplateView , ListView , CreateView , UpdateView , DeleteView, DetailView
from .models import Table

class curd_table_view(ListView):
    template_name = 'Apptable/table_list.html'
    model = Table
    context_object_name = 'tables'
    queryset = Table.objects.all()

class Tabledetail(DetailView):
    model = Table
    template_name = 'Apptable/table_detail.html'
    context_object_name = 'tables_detail'


class createtable(CreateView):
    template_name = 'Apptable/table_create.html'
    model = Table
    fields = '__all__'

class Tableupdate(UpdateView):
    template_name = 'Apptable/table_update.html' 
    model = Table 
    fields = '__all__'

class TableDelete(DeleteView):
    template_name = 'Apptable/table_delete.html'
    model = Table