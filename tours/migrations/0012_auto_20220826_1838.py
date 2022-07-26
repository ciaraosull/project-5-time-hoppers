# Generated by Django 3.2.14 on 2022-08-26 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0011_auto_20220826_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='accessibility_friendly',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='quantity',
            field=models.PositiveSmallIntegerField(help_text='Number of TimeHoppers over 18 years old only'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_duration',
            field=models.CharField(help_text='Specify quantity by days or hours only', max_length=250, null=True),
        ),
    ]
