# Generated by Django 4.2.13 on 2024-05-21 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_depositproduct_fin_co_subm_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositoption',
            name='intr_rate',
            field=models.FloatField(null=True),
        ),
    ]