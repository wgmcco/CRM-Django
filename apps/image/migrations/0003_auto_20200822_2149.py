# Generated by Django 3.0.8 on 2020-08-22 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_auto_20200822_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_image',
            field=models.ImageField(blank=True, default='image/default.jpg', null=True, upload_to='image/name/'),
        ),
    ]
