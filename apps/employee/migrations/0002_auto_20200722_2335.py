# Generated by Django 3.0.8 on 2020-07-22 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emergency_contact',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emergency_phone',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(blank=True, max_length=14),
        ),
    ]
