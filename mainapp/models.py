from django.conf import settings
from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts", on_delete=models.CASCADE)
    body = models.TextField()
