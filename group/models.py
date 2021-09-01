import random
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField
# from students.models import Student
from teachers.models import Teacher
from faker import Faker

class Group(models.Model):
    descipline = models.CharField(max_length=200)
    hours_to_take = models.IntegerField(default=32)
    headman = models.ForeignKey('students.Student', null=True, unique=False, on_delete=models.CASCADE, related_name="headed_group")
    curator = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True,)

    @classmethod
    def _gen(cls):
        fake = Faker()
        gr = Group(
            descipline= fake.word() + 'ology',
            hours_to_take = random.randint(20,40)
        )
        gr.save()
        return gr