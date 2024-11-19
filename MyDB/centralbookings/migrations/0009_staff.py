# Generated by Django 5.1.3 on 2024-11-19 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centralbookings', '0008_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('ID_Number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='centralbookings.participant')),
                ('Position', models.CharField(max_length=100)),
            ],
        ),
    ]
