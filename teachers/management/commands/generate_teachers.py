# noqa: D102, A003
import random

from django.core.management.base import BaseCommand

from group.models import Group

from students.models import Student

from teachers.models import Teacher


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('number_of_teachers', nargs='?', type=int, default=100)

    def handle(self, *args, **options):
        teachers_list = [Teacher._gen() for _ in range(options['number_of_teachers'])]
        groups_list = []
        for teacher in teachers_list:
            teacher.group_set.add(Group._gen())
            groups_list.append(teacher.group_set.all().get())
        for group in groups_list:
            sostav = []
            for _ in range(random.randint(1, 10)):
                group.student_in_group.add(Student._gen())
            sostav.append(list(group.student_in_group.all()))
            group.headman = sostav[0][0]
            group.save()
        self.stdout.write(self.style.SUCCESS('Successfully created teachers'))
