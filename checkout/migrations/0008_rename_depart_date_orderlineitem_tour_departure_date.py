# Generated by Django 3.2.14 on 2022-09-25 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_remove_orderlineitem_tour_departure_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='depart_date',
            new_name='tour_departure_date',
        ),
    ]
