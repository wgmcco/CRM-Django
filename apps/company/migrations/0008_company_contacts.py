# Generated by Django 3.0.8 on 2020-08-01 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_auto_20200801_1933'),
        ('company', '0007_remove_company_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='contacts',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contact.Contact'),
            preserve_default=False,
        ),
    ]
