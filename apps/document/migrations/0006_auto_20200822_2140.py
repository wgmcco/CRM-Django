# Generated by Django 3.0.8 on 2020-08-22 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0005_auto_20200809_0049'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='document',
            order_with_respect_to='company',
        ),
    ]
