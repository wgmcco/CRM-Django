# Generated by Django 3.0.8 on 2020-09-06 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0005_auto_20200829_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='agency_name',
            field=models.CharField(max_length=50),
        ),
    ]