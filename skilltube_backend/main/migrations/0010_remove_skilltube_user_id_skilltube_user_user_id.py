# Generated by Django 4.2.1 on 2023-06-09 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_skilltube_user_user_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skilltube_user',
            name='id',
        ),
        migrations.AddField(
            model_name='skilltube_user',
            name='user_id',
            field=models.UUIDField(default='43a882e848224491a9da77aec643f63d', editable=False, primary_key=True, serialize=False),
        ),
    ]
