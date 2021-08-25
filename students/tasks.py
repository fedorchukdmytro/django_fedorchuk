from random import randrange
from time import sleep

from celery import shared_task
from faker import Faker
from django.core.mail import send_mail

from .models import Student
from django.utils.crypto import get_random_string

fake = Faker()


@shared_task
def st_generate(total):
    for i in range(total):
        sleep(10)
        first_name = 'user_{}'.format(get_random_string(10))
        last_name = 'user_{}'.format(get_random_string(10))
        age = randrange(20,60)
        Student.objects.create(first_name=first_name, last_name=last_name, age=age)
    return '{} random users created with success!'.format(total)
    
    


@shared_task
def beat():
    print('beat START')
    sleep(5)
    print('beat END')