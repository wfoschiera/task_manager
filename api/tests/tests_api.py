from django_assertions import assert_equal
from django.test import Client


resp_json = b'{"List":"/task-list/","Detail View":"/task-detail/\
<str:pk>/","Create":"/task-create/","Update":"/task-update/<str:pk>/\
","Delete":"/task-delete/<str:pk>/"}'


def test_api_home(client: Client):
    resp = client.get('/api/')
    assert resp.status_code == 200


def test_api_overview(client: Client):
    resp = client.get('/api/')
    content = resp.content
    assert_equal(resp_json, content)


def test_task_detail(client: Client):
    resp = client.get('/api/task-detail/')  # incluir str:pk
    content = resp.content
    yield content
