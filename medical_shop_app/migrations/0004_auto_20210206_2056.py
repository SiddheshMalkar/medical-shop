# Generated by Django 3.1.6 on 2021-02-06 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medical_shop_app', '0003_auto_20210206_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='mid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical_shop_app.medicine'),
        ),
    ]
