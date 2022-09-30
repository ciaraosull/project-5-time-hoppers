# Generated by Django 3.2.14 on 2022-09-30 21:29

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tours', '0030_remove_tour_departure_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, unique=True)),
                ('profile_image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
                ('multi_lingual', models.BooleanField(blank=True, null=True)),
                ('date_started', models.DateField()),
                ('faviourite_era', models.TextField()),
                ('social_media_link', models.URLField(blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('tour', models.ForeignKey(blank=True, help_text='Specify tour this staff member is currently working on', null=True, on_delete=django.db.models.deletion.SET_NULL, to='tours.tour')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]
