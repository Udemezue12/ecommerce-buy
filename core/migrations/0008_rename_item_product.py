# Generated by Django 5.0.1 on 2024-01-19 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_shipping_address_order_address'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='Product',
        ),
    ]
