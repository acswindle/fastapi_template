from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Welcome to FastAPI" in response.text
    assert "/static/styles.css" in response.text


def test_static_file():
    response = client.get("/static/styles.css")
    assert response.status_code == 200
    assert "text/css" in response.headers["content-type"]
