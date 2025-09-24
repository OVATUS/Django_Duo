from django.shortcuts import render

# Create your views here.
def curd_table(request):
    return render(request, 'curd_table.html')