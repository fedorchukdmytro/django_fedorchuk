# Create your tests here.
from django.test import Client

import pytest

from ..models import Student


def test_error_404():
    c = Client()
    response = c.get('sgfsgfdg/')
    assert response.status_code == 404


def test_index_view():
    c = Client()
    response = c.get('')
    assert response.status_code == 200


def test_error_500():
    c = Client()
    response = c.get('check/')
    assert response.status_code == 404


@pytest.mark.django_db
def test_students_list():
    c = Client()
    response = c.get('/list-students/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_base_query():
    assert Student.objects.count() == 0


@pytest.mark.django_db
def test_generate_students():
    c = Client()
    c.get('/generate-students/?count=100')
    assert Student.objects.count() == 100


@pytest.mark.django_db
def test_create_student():
    c = Client()
    url = '/create-student/'
    c.post(url, data={'first_name': 'Dmytro',
                      'last_name': 'Fedorchuk',
                      'age': 37,
                      'phone': '38067444167000'
                      }
           )
    assert Student.objects.filter(first_name='Dmytro',
                                  last_name='Fedorchuk',
                                  )
    assert Student.objects.count() == 1


@pytest.mark.django_db
def test_edit_student():
    c = Client()
    Student._gen()
    assert Student.objects.count() == 1
    response = c.post('/edit-student/1/', data={'last_name': 'Clinton',
                                                'first_name': 'Bill',
                                                'age': 57,
                                                'phone': '06755544455433'
                                                }
                      )
    assert response.status_code == 302
    assert 'Clinton' == Student.objects.get(id=1).last_name


@pytest.mark.django_db
def test_logging_admin(client):
    response = client.get('/admin/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_deleting_student(client):
    Student._gen()
    assert Student.objects.count() == 1
    client.post('/delete-student/1/')
    assert Student.objects.count() == 0
