from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    story = models.TextField(blank=True, null=True)
    cat_image = models.ImageField(upload_to='cat/')
    
    riddle = models.TextField(null=True)
    riddle_image = models.ImageField(upload_to='riddle/')
    hint = models.CharField(blank=True, max_length=200)

    post_url = models.CharField(null=True, max_length=50)
    next_url = models.CharField(null=True, max_length=50)
    postProgress = models.IntegerField(default=0)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    asdf = 5

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.asdf = 3
        print(self.asdf)
        super().save(*args, **kwargs)