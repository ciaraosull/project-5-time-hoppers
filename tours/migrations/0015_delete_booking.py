# Generated by Django 3.2.14 on 2022-08-29 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0014_alter_booking_notes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]