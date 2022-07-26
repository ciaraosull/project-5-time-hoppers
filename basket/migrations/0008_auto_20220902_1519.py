# Generated by Django 3.2.14 on 2022-09-02 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basket', '0007_bookingitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookingitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
