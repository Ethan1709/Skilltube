from django.db import models
import uuid

# Create your models here.

class Video(models.Model):
    video_title = models.CharField(max_length=255)
    video_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video_path = models.CharField(max_length=255)
    thumbnail = models.ForeignKey('Thumbnail', on_delete=models.CASCADE)


class Thumbnail(models.Model):
    thumbnail_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    thumbnail_path = models.CharField(max_length=255)
