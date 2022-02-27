# Following Codemy.com django blog tutorial from youtube, blending it with bouique ado structre.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '|' + str(self.author)
