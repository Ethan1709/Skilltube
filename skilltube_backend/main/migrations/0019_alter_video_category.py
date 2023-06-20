# Generated by Django 4.2.1 on 2023-06-20 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_video_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='category',
            field=models.CharField(choices=[('Noob', 'Noob'), ('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Masterclass', 'Masterclass')], default='Beginner', max_length=20),
        ),
    ]
