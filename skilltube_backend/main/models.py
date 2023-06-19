from django.db import models
import uuid
from datetime import datetime

# Create your models here.

class Video(models.Model):
    CATEGORY_CHOICES = [
        ('noob', 'Noob'),
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('masterclass', 'Masterclass'),
    ]
    caption = models.CharField(max_length=255)
    video_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video = models.FileField(upload_to='main/%y')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    created_at = models.DateTimeField(default=datetime.now)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='beginner')

    def __str__(self):
        return self.caption
    
    def save(self, *args, **kwargs):
        if not self.category:
            self.category = 'beginner'
        super().save(*args, **kwargs)
    