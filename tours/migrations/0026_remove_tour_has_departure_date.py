# Generated by Django 3.2.14 on 2022-09-25 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0025_tour_departure_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='has_departure_date',
        ),
    ]
