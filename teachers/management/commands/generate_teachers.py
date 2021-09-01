# noqa: D102, A003
from group.models import Group
from random import randrange, randint
import random
from django.core.management.base import BaseCommand

from faker import Faker


from teachers.models import Teacher

from students.models import Student

from group.models import Group

class Command(BaseCommand):
    # help = 'Genereates random teacherss base on input amount'

    def add_arguments(self, parser):
        parser.add_argument('number_of_teachers', nargs='?', type=int, default=100)

    def handle(self, *args, **options):
        f = Faker()
        
        teachers_list = [Teacher.gen() for _ in range(options['number_of_teachers'])]
         
        groups_list = []
        for teacher in teachers_list:
            groups_list.append(teacher.group_set.create(descipline=str(f.job()) + 'ology',
                                                 hours_to_take=randrange(32, 40),
                                                 headman= Student.gen()))
        
        for group in groups_list:
            sostav = []
            for _ in range(9):
                    sostav.append(group.student_in_group.add(Student.gen()))
            group.student_in_group.add(group.headman)
        
       
        
        self.stdout.write(self.style.SUCCESS('Successfully created teachers'))


 
        # for _ in range(options['number_of_teachers']):
           