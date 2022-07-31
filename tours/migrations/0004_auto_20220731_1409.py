# Generated by Django 3.2.14 on 2022-07-31 14:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_auto_20220731_1359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tour',
            options={'ordering': ['-date_added']},
        ),
        migrations.AddField(
            model_name='tour',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
