import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models import books_db

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_db():
    books_db.clear()
    yield
    books_db.clear()


def test_create_book():
    response = client.post("/books/", json={"title": "Test Book", "author": "Author"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Book"
    assert data["author"] == "Author"
    assert "id" in data


def test_get_books():
    client.post("/books/", json={"title": "Book1", "author": "Author1"})
    response = client.get("/books/")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_book():
    create_response = client.post(
        "/books/", json={"title": "Book2", "author": "Author2"}
    )
    book_id = create_response.json()["id"]
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Book2"


def test_update_book():
    create_response = client.post(
        "/books/", json={"title": "Book3", "author": "Author3"}
    )
    book_id = create_response.json()["id"]
    response = client.put(f"/books/{book_id}", json={"title": "Updated Title"})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"


def test_delete_book():
    create_response = client.post(
        "/books/", json={"title": "Book4", "author": "Author4"}
    )
    book_id = create_response.json()["id"]
    response = client.delete(f"/books/{book_id}")
    assert response.status_code == 200
    get_response = client.get(f"/books/{book_id}")
    assert get_response.status_code == 404
