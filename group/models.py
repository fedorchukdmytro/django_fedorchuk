from django.db import models


class Group(models.Model):
    descipline = models.CharField(max_length=200)
    hours_to_take = models.IntegerField(default=32)
