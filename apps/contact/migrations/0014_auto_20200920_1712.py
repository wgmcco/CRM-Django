# Generated by Django 3.0.8 on 2020-09-20 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0013_auto_20200906_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='profile_image',
            field=models.ImageField(blank=True, default='contact/default_person.png', null=True, upload_to='contact/'),
        ),
    ]
