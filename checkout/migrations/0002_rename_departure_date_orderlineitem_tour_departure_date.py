# Generated by Django 3.2.14 on 2022-09-13 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='departure_date',
            new_name='tour_departure_date',
        ),
    ]