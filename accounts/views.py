from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import SaleForm

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

def makeSale(request):
    form = SaleForm()
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'accounts/makesale.html', context)

# The update order function
def updateSale(request, pk):
    sale = Sale.objects.get(id=pk)
    form = SaleForm(instance=sale)
    if request.method == 'POST':
        form = SaleForm(request.POST, instance= sale)
        if form.is_valid():
            form.save()
            return redirect('/sales')
    context = {'form': form}
    return render(request, 'accounts/makesale.html', context)


# Delete Sale function
def deleteSale(request, pk):
    sale = Sale.objects.get(id=pk)
    if request.method == "POST":
        sale.delete()
        return redirect('/sales')
    context = {'sale':sale}
    return render(request, 'accounts/delete.html', context)
    
 