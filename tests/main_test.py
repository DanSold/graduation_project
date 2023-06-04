import pytest

from fastapi.testclient import TestClient
from fastapi import status

import sys
import os


@pytest.fixture()
def client():
    print(sys.path)
    print(os.getcwdb().decode("utf-8"))
    sys.path.append(os.getcwdb().decode("utf-8").replace('\\', '\\\\'))
    from main import app
    print(sys.path)
    with TestClient(app) as client:
        yield client


def test_root(client: TestClient):
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'message': 'root endpoint'}


def test_number_reducer_positive(client: TestClient):
    response = client.get('/100')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'message': 'ok',
        'result': 50.0,
    }


def test_number_reducer_with_wrong_query(client: TestClient):
    response = client.get('/100?query=kk')
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
