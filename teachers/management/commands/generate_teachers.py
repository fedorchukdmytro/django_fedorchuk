from random import randrange

from django.core.management.base import BaseCommand, CommandError
from teachers.models import Teacher

from faker import Faker


class Command(BaseCommand):
    help = 'Genereates random teacherss base on input amount'

    def add_arguments(self, parser):
        parser.add_argument('number_of_teachers', nargs='?', type=int, default = 100)

    def handle(self, *args, **options):
        fake = Faker()
        result = []

        for _ in range(options['number_of_teachers']):
            result.append(Teacher(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=randrange(1,99)
            ))
        Teacher.objects.bulk_create(result)

        self.stdout.write(self.style.SUCCESS('Successfully created teachers'))