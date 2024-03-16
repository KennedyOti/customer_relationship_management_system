from django.urls import path
from . import views

# URL Paths that implement routiing

urlpatterns = [
    path('', views.homepage),
    path('products/', views.products),
    path('customers/', views.customers),
]
