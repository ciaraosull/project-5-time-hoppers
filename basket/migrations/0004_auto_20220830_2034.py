# Generated by Django 3.2.14 on 2022-08-30 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0003_auto_20220830_2019'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'ordering': ['-date_added']},
        ),
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-date_added']},
        ),
        migrations.RenameField(
            model_name='basket',
            old_name='date_ordered',
            new_name='date_added',
        ),
    ]
