# Generated by Django 5.0.3 on 2024-04-04 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, null=True)),
                ('product_type', models.CharField(max_length=200, null=True)),
                ('product_qtty', models.IntegerField(null=True)),
                ('product_bp', models.IntegerField(null=True)),
                ('product_sp', models.IntegerField(null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]