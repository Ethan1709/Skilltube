from django.db import models
import uuid
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Count

# Create your models here.

class Video(models.Model):
    CATEGORY_CHOICES = [
        ('Noob', 'Noob'),
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Masterclass', 'Masterclass'),
    ]
    caption = models.CharField(max_length=255)
    video_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video = models.FileField(upload_to='main/%y')
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images/')
    created_at = models.DateTimeField(default=datetime.now)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Beginner')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.caption
    
    def save(self, *args, **kwargs):
        if not self.category:
            self.category = 'Beginner'
        super().save(*args, **kwargs)


class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.video.caption}'
    

class Like(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('video', 'user')

    @property
    def like_count(self):
        return self.video.likes.count()