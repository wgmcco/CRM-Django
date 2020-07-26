# Generated by Django 3.0.8 on 2020-07-26 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20200726_2214'),
        ('employee', '0009_remove_employee_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='company.Company'),
            preserve_default=False,
        ),
    ]