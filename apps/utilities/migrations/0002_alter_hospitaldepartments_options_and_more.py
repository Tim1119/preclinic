# Generated by Django 4.2.3 on 2023-08-08 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hospitaldepartments',
            options={'verbose_name': 'Hospital Departments', 'verbose_name_plural': 'Hospital Departments'},
        ),
        migrations.AlterModelOptions(
            name='workexperience',
            options={'verbose_name': 'Work Experience', 'verbose_name_plural': 'Work Experience'},
        ),
    ]
