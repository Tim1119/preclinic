# Generated by Django 4.2.3 on 2023-08-13 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0006_alter_doctorappointment_ailment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ['-created_at']},
        ),
    ]
