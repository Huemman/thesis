from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    authors = models.CharField(max_length=200)
    adviser = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    astract = models.TextField()


    def __str__(self):
        return self.title

