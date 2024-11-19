# Generated by Django 5.1.3 on 2024-11-19 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centralbookings', '0002_organizer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internal',
            fields=[
                ('Organizer_ID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='centralbookings.organizer')),
                ('Organizer_Department', models.CharField(max_length=100)),
            ],
        ),
    ]
