from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import SaleForm, CreateUserForm
from .filters import SaleFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group

# Create your views here.

# This function renders homepage
@login_required(login_url='signin')
@admin_only
def homepage(request):
    return render(request, 'accounts/dashboard.html')

# This function renders the product page
@login_required(login_url='signin')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Products.objects.all()
    return render(request, 'accounts/products.html', {'products':products})

# This function renders the sales page
@login_required(login_url='signin')
def sales(request):
    sales = Sale.objects.all()
    myFilter = SaleFilter(request.GET, queryset=sales)
    sales = myFilter.qs
    context = {'sales':sales,'myFilter':myFilter}
    return render(request, 'accounts/sales.html', context)

# This function renders the reports page
@login_required(login_url='signin')
@allowed_users(allowed_roles=['admin'])
def reports(request):
    return render(request, 'accounts/reports.html')

@login_required(login_url='signin')
def makeSale(request):
    form = SaleForm()
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sales')
    context = {'form':form}
    return render(request, 'accounts/makesale.html', context)

# The update order function
@login_required(login_url='signin')
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
@login_required(login_url='signin')
def deleteSale(request, pk):
    sale = Sale.objects.get(id=pk)
    if request.method == "POST":
        sale.delete()
        return redirect('/sales')
    context = {'sale':sale}
    return render(request, 'accounts/delete.html', context)

# sign un function
@unauthenticated_user
def signup(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        
        form = CreateUserForm()  # Initialize form here

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                group = Group.objects.get(name='employee')
                user.groups.add(group)
                messages.success(request, 'Account Created Successfully For'+ username)

                return redirect('signin')

        context = {'form': form}
        return render(request, 'accounts/signup.html', context)

#sign in function
@unauthenticated_user
def signin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'Username OR Password is Incorrect')

    context = {}
        
    return render(request, 'accounts/signin.html', context)

def signOutUser(request):
    logout(request)
    return redirect('signin')

def employeePage(request):
    return render(request, 'accounts/employee.html')