# Generated by Django 3.0.8 on 2020-07-26 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='profile_image',
            field=models.ImageField(blank=True, default='contact/default.jpg', null=True, upload_to='contact/'),
        ),
    ]
