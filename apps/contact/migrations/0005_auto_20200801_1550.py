# Generated by Django 3.0.8 on 2020-08-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20200726_2224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='contact',
            name='fax',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='contact',
            unique_together={('first_name', 'last_name')},
        ),
    ]
