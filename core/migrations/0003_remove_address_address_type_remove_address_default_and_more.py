# Generated by Django 5.0.1 on 2024-01-19 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_address_address_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='address_type',
        ),
        migrations.RemoveField(
            model_name='address',
            name='default',
        ),
        migrations.RemoveField(
            model_name='address',
            name='zip',
        ),
    ]
