# Generated by Django 5.1.3 on 2024-11-19 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centralbookings', '0006_participant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('ID_Number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='centralbookings.participant')),
                ('Year_Level', models.IntegerField(default=1)),
                ('Program', models.CharField(max_length=100)),
            ],
        ),
    ]
