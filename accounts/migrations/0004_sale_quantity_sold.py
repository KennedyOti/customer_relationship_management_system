# Generated by Django 5.0.3 on 2024-04-04 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_sale_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='quantity_sold',
            field=models.IntegerField(null=True),
        ),
    ]
