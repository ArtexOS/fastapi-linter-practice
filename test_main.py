from fastapi.testclient import TestClient
from httpx import Response

from .main import app

client = TestClient(app)


def test_read_root():
    response: Response = client.get("/hello?name=Tester")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Tester"}
