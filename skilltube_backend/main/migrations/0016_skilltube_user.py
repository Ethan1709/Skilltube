# Generated by Django 4.2.1 on 2023-06-10 21:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_delete_skilltube_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skilltube_user',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
    ]