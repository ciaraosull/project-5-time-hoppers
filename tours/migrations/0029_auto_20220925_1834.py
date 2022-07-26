# Generated by Django 3.2.14 on 2022-09-25 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0028_alter_tour_departure_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='has_departure_time',
            new_name='departure_time',
        ),
        migrations.AddField(
            model_name='tour',
            name='has_departure_date',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
