# Generated by Django 3.0.8 on 2020-08-01 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_contact_com'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='com',
            new_name='company',
        ),
    ]