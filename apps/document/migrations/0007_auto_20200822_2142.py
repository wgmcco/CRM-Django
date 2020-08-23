#nerated by Django 3.0.8 on 2020-08-22 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0006_auto_20200822_2140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ('company',), 'verbose_name': 'Document', 'verbose_name_plural': 'Documents'},
        ),
        migrations.AlterOrderWithRespectTo(
            name='document',
            order_with_respect_to=None,
        ),
    ]
