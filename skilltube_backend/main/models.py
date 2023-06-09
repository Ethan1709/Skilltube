from django.db import models
from django import forms
import uuid
from datetime import datetime
from django.core.validators import MinLengthValidator

# Create your models here.

class Video(models.Model):
    caption = models.CharField(max_length=255)
    video_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video = models.FileField(upload_to='main/%y')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.caption


class Skilltube_user(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4().hex, editable=False, unique=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.pk = self.user_id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username