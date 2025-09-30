from django.shortcuts import render
from django.views.generic import TemplateView , ListView , CreateView , UpdateView , DeleteView, DetailView
from uiuser.models import Table
from .models import MenuItem
from django.urls import reverse_lazy
# Table CRUD
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
    success_url = reverse_lazy('curd_table')

class Tableupdate(UpdateView):
    template_name = 'Apptable/table_update.html' 
    model = Table 
    fields = '__all__'
    success_url = reverse_lazy('curd_table')

class TableDelete(DeleteView):
    template_name = 'Apptable/table_delete.html'
    model = Table
    success_url = reverse_lazy('curd_table')

class testview(TemplateView):
    template_name = 'Apptable/test.html'
   
# Food CRUD

class foodlist(ListView):
    model = MenuItem
    context_object_name = 'foodlist'
    template_name = 'Appfood/food_list.html'
    queryset = MenuItem.objects.all()

class fooddetail(DetailView):
    model = MenuItem
    template_name = 'Appfood/food_detail.html'
    context_object_name = 'food_detail'
    queryset = MenuItem.objects.all()

class createfood(CreateView):
    template_name = 'Appfood/food_create.html'
    model = MenuItem
    fields = '__all__'
    success_url = reverse_lazy('food_list')

class foodupdate(UpdateView):
    template_name = 'Appfood/food_update.html' 
    model = MenuItem 
    fields = '__all__'
    success_url = reverse_lazy('food_list')

class foodDelete(DeleteView):
    template_name = 'Appfood/food_delete.html'
    model = MenuItem
    success_url = reverse_lazy('food_list')
