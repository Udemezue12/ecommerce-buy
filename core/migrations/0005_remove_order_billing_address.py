# Generated by Django 5.0.1 on 2024-01-19 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_address_address_type_address_default_address_zip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='billing_address',
        ),
    ]
