# Generated by Django 3.0.8 on 2020-08-01 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_company_people'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='people',
            new_name='contacts',
        ),
    ]
