# Generated by Django 3.1.2 on 2020-12-18 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20201217_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ship_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ship_phone',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_amount',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='product_price',
        ),
    ]