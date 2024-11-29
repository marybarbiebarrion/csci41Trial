# Generated by Django 5.1.3 on 2024-11-28 18:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centralbookings', '0013_participant_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='centralbookings.participant')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
