from django.db import models

from user.models import User


class Event(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    date = models.DateTimeField(auto_created=True)
    location = models.CharField(max_length=256)
    creator = models.ForeignKey(User, on_delete=models.CASCADE ,  related_name='created_events')
    invited_user = models.ManyToManyField(User ,  related_name="invited_events" , blank=True)

