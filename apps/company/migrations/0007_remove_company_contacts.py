# Generated by Django 3.0.8 on 2020-08-01 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_auto_20200801_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='contacts',
        ),
    ]