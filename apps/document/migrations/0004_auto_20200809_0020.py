# Generated by Django 3.0.8 on 2020-08-09 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0003_auto_20200801_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='pdf',
            field=models.ImageField(blank=True, null=True, upload_to='document/'),
        ),
    ]
