# Generated by Django 3.2.14 on 2022-09-25 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='depart_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
