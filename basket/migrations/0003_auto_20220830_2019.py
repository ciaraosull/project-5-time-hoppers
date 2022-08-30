# Generated by Django 3.2.14 on 2022-08-30 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basket', '0002_booking_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booked',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('booked', models.BooleanField(default=False)),
                ('booking_items', models.ManyToManyField(to='basket.Booking')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
