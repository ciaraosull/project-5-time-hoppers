# Generated by Django 3.2.14 on 2022-10-04 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_staffmember_contact_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffmember',
            name='social_media_link',
        ),
    ]
