# Generated by Django 4.2.1 on 2023-06-06 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
