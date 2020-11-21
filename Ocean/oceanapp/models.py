from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class oceanappmodel(models.Model):
    title = models.CharField(max_length=200, unique=True)
    location = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='ocean_drops')
    caption = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title