# Generated by Django 5.1 on 2024-10-04 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valorizacion', '0002_rename_neighborhood_property_neighbourhood_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='direccion',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
