from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import AbstractUser
from movies.models import Movie

class User(AbstractUser):
    first_name = None
    last_name = None
    age = models.IntegerField(default=0)

class UserMovie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    liked = models.BooleanField()
    disliked = models.BooleanField()
    wished = models.BooleanField()
    watched = models.BooleanField()
    review = models.BooleanField()