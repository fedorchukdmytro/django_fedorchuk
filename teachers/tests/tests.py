
from django.test import Client

import pytest

from ..models import Teacher


@pytest.mark.django_db
def test_list_teachers():
    c = Client()
    response = c.get('/list-teachers/')
    assert response.status_code == 200
    assert Teacher.objects.count() == 0


@pytest.mark.django_db
def test_adding_teachers():
    c = Client()
    assert Teacher.objects.count() == 0
    Teacher._gen()
    response = c.get('/list-teachers/')
    assert response.status_code == 200
    assert Teacher.objects.count() == 1


@pytest.mark.django_db
def test_delete():
    c = Client()
    assert Teacher.objects.count() == 0
    Teacher._gen()
    assert Teacher.objects.count() == 1
    c.post('/delete-teacher/1/')
    assert Teacher.objects.count() == 0


@pytest.mark.django_db
def test_create_teacher():
    c = Client()
    assert Teacher.objects.count() == 0
    response = c.post('/create-teacher/', data={'last_name': 'George',
                                                'first_name': 'Bush',
                                                'Age': 52
                                                }
                      )
    assert response.status_code == 200
    Teacher.objects.count() == 1


@pytest.mark.django_db
def test_eddit_teacher():
    c = Client()
    assert Teacher.objects.count() == 0
    response = c.post('/create-teacher/', data={'last_name': 'Jordan',
                                                'first_name': 'Micheal',
                                                'age': 52})
    assert response.status_code == 302
    assert Teacher.objects.count() == 1
