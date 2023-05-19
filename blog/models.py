from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    redacted_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title