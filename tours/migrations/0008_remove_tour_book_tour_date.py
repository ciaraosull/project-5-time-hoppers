# Generated by Django 3.2.14 on 2022-08-26 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0007_tour_book_tour_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='book_tour_date',
        ),
    ]
