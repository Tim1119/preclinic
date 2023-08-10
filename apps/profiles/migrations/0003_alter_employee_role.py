# Generated by Django 4.2.3 on 2023-08-10 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_employee_date_of_birth_employee_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.CharField(choices=[('Nurse', 'Nurse'), ('Pharmacist', 'Pharmacist'), ('Laboratorist', 'Laboratorist'), ('Accountant', 'Accountant'), ('Receptionist', 'Receptionist'), ('Doctor', 'Doctor')], max_length=40),
        ),
    ]
