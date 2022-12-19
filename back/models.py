from pickle import FALSE
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import clear_script_prefix
import uuid
import os


def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images/', filename)

class MyUser(User):
    def __str__(self) -> str:
        return self.username

class Images(models.Model):
    photo_path = user_directory_path
    image = models.ImageField(upload_to=photo_path, default='post/default.jpg')
    created = models.DateTimeField(default=timezone.now)
    mac = models.TextField(blank=FALSE)
    id = models.IntegerField(primary_key=True)
    img_data = models.TextField(blank=True)