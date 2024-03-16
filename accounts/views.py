from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# This function renders homepage
def homepage(request):
    return render(request, 'accounts/dashboard.html')

# This function renders the product page
def products(request):
    return render(request, 'accounts/products.html')

# This function renders the customers page
def customers(request):
    return render(request, 'accounts/customers.html')
