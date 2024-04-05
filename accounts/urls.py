from django.urls import path
from . import views

# URL Paths that implement routiing

urlpatterns = [
    path('', views.homepage, name= 'homepage'),
    path('products/', views.products, name='products'),
    path('sales/', views.sales, name='sales'),
    path('reports/', views.reports, name='reports'),
]
