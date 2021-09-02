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
        
        teachers_list = [Teacher._gen() for _ in range(options['number_of_teachers'])]
         
        groups_list = []
        for teacher in teachers_list:
            teacher.group_set.add(Group._gen())
            groups_list.append(teacher.group_set.all().get())
        
        for group in groups_list:
            # breakpoint()
            sostav = []
            print(group.id)
            for _ in range(random.randint(1, 10)):
                group.student_in_group.add(Student._gen())   
            sostav.append(list(group.student_in_group.all()))
            
            group.headman = sostav[0][0]
            group.save() # print(sostav)
            a = group
            print(sostav[0][0])
            print(a.headman)
            print(a.headman.id)
            
           
        
       
        
        self.stdout.write(self.style.SUCCESS('Successfully created teachers'))


 
        # for _ in range(options['number_of_teachers']):
           