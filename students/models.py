import random

from django.db import models

from faker import Faker

from group.models import Group

YEAR_IN_SCHOOL_CHOICES = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
]


class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'), ]

    first_name = models.CharField(max_length=200, verbose_name='ИМЯ')
    last_name = models.CharField(max_length=200, verbose_name='ФАМИЛИЯ')
    age = models.IntegerField(default=18, verbose_name='ВОЗРАСТ')
    phone = models.CharField(max_length=15, null=True, verbose_name='НОМЕР ТЕЛЕФОНА', blank=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, verbose_name='СОСТОИТ В ГРУППЕ', null=True, blank=True)
    status = models.CharField(blank=True,
                              max_length=2,
                              verbose_name='ГОД ОБУЧЕНИЯ',
                              choices=YEAR_IN_SCHOOL_CHOICES,
                              default=FRESHMAN
                              )

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.age} {self.phone} {self.status}"

    @classmethod
    def _gen(cls):
        fake = Faker()
        st = cls(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=random.randint(18, 100),
            phone=fake.msisdn(),
            status=random.choices(YEAR_IN_SCHOOL_CHOICES)[0][0]
        )
        st.save()
        return st

    def submissive_group(self):
        sub = self.headed_group.all().get()
        return sub
    submissive_group.short_description = 'СТАРОСТА ГРУППЫ'

    def total_students_in_his_group(self):
        his_group = self.group
        if self.group is not None:
            total = his_group.student_set.all()
            fug = []
            for i in total:
                fug.append(i.last_name)
            return fug
        else:
            pass
    total_students_in_his_group.short_description = 'ОДНОГРУПНИКИ'

    # def save(self, *args, **kwargs):
    #     # breakpoint()
    #     super(Student, self).save(*args, **kwargs)
    #     st_num = int(len(self.group.student_in_group.all()))
    #     self.group.number_of_students_engaged = st_num
    #     self.group.save()

    # def delete(self, *args, **kwargs):
    #     # breakpoint()
    #     super(Student, self).delete(*args, **kwargs)
    #     st_num = int(len(self.group.student_in_group.all()))
    #     self.group.number_of_students_engaged = st_num
    #     self.group.save()


class Logger(models.Model):
    method = models.CharField(max_length=6)
    path = models.CharField(max_length=30)
    execution_time = models.DecimalField(max_digits=15, decimal_places=10)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.method} {self.path} {self.execution_time}"
