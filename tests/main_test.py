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
    assert response.json() == {'res': 'res'}
