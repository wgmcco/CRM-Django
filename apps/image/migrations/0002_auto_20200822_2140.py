# Generated by Django 3.0.8 on 2020-08-22 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('equip_number',), 'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
    ]
