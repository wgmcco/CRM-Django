# Generated by Django 3.0.8 on 2020-08-29 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0003_auto_20200801_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='fax',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
