from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator


class Group(models.Model):
    descipline= models.CharField(max_length=200)
    hours_to_take = models.IntegerField(validators=[MaxValueValidator(30),MinValueValidator(10)])
    
