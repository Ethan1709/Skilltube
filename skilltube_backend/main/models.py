from django.db import models
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
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50, validators=[MinLengthValidator(8)])
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.user_id