# Generated by Django 3.0.8 on 2020-08-01 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20200801_1635'),
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='insurance',
            unique_together={('company', 'type')},
        ),
    ]
