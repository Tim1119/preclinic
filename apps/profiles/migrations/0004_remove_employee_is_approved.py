# Generated by Django 4.2.3 on 2023-08-13 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_employee_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='is_approved',
        ),
    ]
