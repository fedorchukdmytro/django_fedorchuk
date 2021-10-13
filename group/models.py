import random

from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField

from faker import Faker

from teachers.models import Teacher
# from students.models import Student


class Group(models.Model):
    descipline = models.CharField(max_length=200)
    hours_to_take = models.IntegerField(default=32)
    headman = models.ForeignKey('students.Student',blank=True, null=True, unique=False, on_delete=models.CASCADE, related_name="headed_group")    # noqa
    curator = models.OneToOneField(Teacher, on_delete=models.CASCADE, null=True, blank=True,)

    def __str__(self) -> str:
        return f" {self.descipline}"

    @classmethod
    def _gen(cls):
        fake = Faker()
        gr = Group(
            descipline=fake.word() + 'ology',
            hours_to_take=random.randint(20, 40)
        )
        gr.save()
        return gr

    def number_of_students_engaged(self):
        sub = len(self.student_set.all())
        return sub

    def total_groups(self):
        # breakpoint()
        fub = self.student_set.all()
        fug = []
        for i in fub:
            fug.append(i.last_name)
        return fug
    total_groups.short_description = 'ФАМИЛИИ УЧАЩИХСЯ'

    def total_groups_in_un(self):
        ttl = len(Group.objects.all())
        return ttl
    total_groups_in_un.short_description = "ВСЕГО ГРУПП В ЭТОЙ ЖОПЕ"
