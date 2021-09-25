import random

from django.db import models

from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=32)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"

    @classmethod
    def _gen(cls):
        fake = Faker()
        tc = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=random.randint(18, 100))
        tc.save()
        return tc

    def submissive_group(self):
        sub = self.group
        return sub
