# Generated by Django 3.0.8 on 2020-07-11 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_profile_social_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='social_number',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
