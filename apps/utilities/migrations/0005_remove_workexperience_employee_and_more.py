# Generated by Django 4.2.3 on 2023-08-13 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0004_delete_ailment_delete_hospitaldepartments_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workexperience',
            name='employee',
        ),
        migrations.DeleteModel(
            name='EducationInformation',
        ),
        migrations.DeleteModel(
            name='WorkExperience',
        ),
    ]
