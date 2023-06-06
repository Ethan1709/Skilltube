from django.db import models
import uuid
from datetime import datetime

# Create your models here.

class Video(models.Model):
    caption = models.CharField(max_length=255)
    video_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video = models.FileField(upload_to='main/%y')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    created_at = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.caption
