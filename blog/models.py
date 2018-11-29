from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    story = models.TextField(blank=True, null=True)
    cat_image = models.ImageField(upload_to='cat/', blank=True)
    
    riddle = models.TextField(null=True)
    riddle_image = models.ImageField(upload_to='riddle/', blank=True)
    hint = models.CharField(blank=True, max_length=200)

    post_url = models.CharField(null=True, max_length=50)
    next_url = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.title