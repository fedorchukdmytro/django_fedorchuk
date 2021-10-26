from django.test import Client

import pytest

from ..models import Group


@pytest.mark.django_db
def test_group_list():
    c = Client()
    response = c.get('/group/list/')
    assert response.status_code == 200
    assert Group.objects.count() == 0


@pytest.mark.django_db
def test_base_query():
    assert Group.objects.count() == 0


@pytest.mark.django_db
def test_create_group():
    c = Client()
    response = c.post('/create-group/', data={'descipline': 'Paleontology',
                                              'hours_to_take': 37})
    assert response.status_code == 302
    assert Group.objects.filter(descipline='Paleontology')
    assert Group.objects.count() == 1


@pytest.mark.django_db
def test_edit_group():
    c = Client()
    Group._gen()
    assert Group.objects.count() == 1
    response = c.post('/edit-group/1/', data={'descipline': 'Nephrology',
                                              'hours_to_take': 37})  # Doesnt want to work without this paprameter
    assert response.status_code == 302
    assert 'Nephrology' == Group.objects.get(id=1).descipline


@pytest.mark.django_db
def test_delete(client):
    Group._gen()
    assert Group.objects.count() == 1
    client.post('/delete-group/1')
    assert Group.objects.count() == 0
