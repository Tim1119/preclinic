# Generated by Django 4.2.3 on 2023-08-08 10:28

import autoslug.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utilities', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ref', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('title', models.CharField(max_length=300, verbose_name="Summarise how you're feeling / ailment")),
                ('appointment_date', models.DateField(verbose_name='Appointment date')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('description', models.TextField(verbose_name="Describe how you're feeling")),
                ('completed', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.patient', verbose_name='created by')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='utilities.hospitaldepartments')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdminAppointment',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='id', unique=True)),
                ('cost', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(limit_value=0, message='Minimum value of cost is 0')])),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Completed', 'Completed')], default='Pending', max_length=260)),
                ('appointment', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appointments.appointment')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]