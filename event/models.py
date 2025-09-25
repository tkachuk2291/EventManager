from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    date = models.DateTimeField(auto_created=True)
    location = models.CharField(max_length=256)
