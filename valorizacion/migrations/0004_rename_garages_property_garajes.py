# Generated by Django 5.1 on 2024-10-04 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valorizacion', '0003_property_direccion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='garages',
            new_name='garajes',
        ),
    ]
