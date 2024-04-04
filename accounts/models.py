from django.db import models

# Create your models here.

# Product Class
class Products (models.Model):
    product_name = models.CharField(max_length=200, null=True)
    product_type = models.CharField(max_length=200, null=True)
    product_qtty = models.IntegerField(null=True)
    product_bp = models.FloatField(null=True)
    product_sp = models.FloatField(null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.product_name
    
# Sales Class

class Sale(models.Model):

    #product=
    date_made = models.DateTimeField(auto_now_add=True, null=True)