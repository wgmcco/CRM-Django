# Generated by Django 3.0.8 on 2020-07-26 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20200726_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='emergency_contact',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AddField(
            model_name='contact',
            name='emergency_phone',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AddField(
            model_name='contact',
            name='social_number',
            field=models.CharField(blank=True, max_length=14),
        ),
    ]
