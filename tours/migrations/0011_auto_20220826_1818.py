# Generated by Django 3.2.14 on 2022-08-26 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0010_booking_departuretime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='departure_time',
            field=models.CharField(choices=[('9:00', '9am'), ('11:00', '11am'), ('13:00', '1pm'), ('15:00', '3pm'), ('20:00', '8pm')], max_length=5),
        ),
        migrations.DeleteModel(
            name='DepartureTime',
        ),
    ]
