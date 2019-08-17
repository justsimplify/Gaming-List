from django.db import models


# Create your models here.
class Games(models.Model):
    title = models.TextField()
    platform = models.TextField()
    score = models.FloatField()
    genre = models.TextField()
    editors_choice = models.CharField(max_length=1)