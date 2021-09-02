from django.db import models
from group.models import Group
from faker import Faker
import random

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=18)
    phone = models.CharField(max_length=15, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name="student_in_group")
    

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.age} {self.phone}"
   
    @classmethod
    def _gen(cls):
        fake = Faker()
        st = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=random.randint(18, 100),
            phone=fake.msisdn())
            
        st.save()
        return st

    def submissive_group(self):
        sub = self.headed_group.all().get()
        return sub


class Logger(models.Model):
    method = models.CharField(max_length=6)
    path = models.CharField(max_length=20)
    execution_time = models.DecimalField(max_digits=15, decimal_places=10)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.method} {self.path} {self.execution_time}"
