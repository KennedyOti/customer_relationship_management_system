from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

# This function renders homepage
def homepage(request):
    return render(request, 'accounts/dashboard.html')

# This function renders the product page
def products(request):
    products = Products.objects.all()
    return render(request, 'accounts/products.html', {'products':products})

# This function renders the sales page
def sales(request):
    sales = Sale.objects.all()
    return render(request, 'accounts/sales.html', {'sales':sales})

# This function renders the reports page
def reports(request):
    return render(request, 'accounts/reports.html')
