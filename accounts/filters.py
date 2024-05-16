import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class SaleFilter(django_filters.FilterSet):
    class Meta:
        model = Sale
        fields = '__all__'
        exclude = ['date_made']