# Generated by Django 3.0.8 on 2020-07-26 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_employee_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='company',
        ),
    ]
