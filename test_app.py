import pytest
from app import app, db, Todo

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_create_todo(client):
    response = client.post("/todos", json={"title": "Learn DevOps"})
    assert response.status_code == 200
    assert response.json["title"] == "Learn DevOps"

def test_get_todos(client):
    client.post("/todos", json={"title": "Test"})
    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json) >= 1
