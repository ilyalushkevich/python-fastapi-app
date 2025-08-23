import allure
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


@allure.feature("Books API")
@allure.story("Create Book")
def test_create_book():
    with allure.step("Send POST request to create book"):
        response = client.post(
            "/books/", json={"title": "Allure Test Book", "author": "Allure Author"}
        )
    with allure.step("Verify response"):
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Allure Test Book"
        allure.attach(
            str(data), name="Response Data", attachment_type=allure.attachment_type.JSON
        )


@allure.feature("Books API")
@allure.story("Get Books")
def test_get_books():
    with allure.step("Create a book first"):
        client.post("/books/", json={"title": "Allure Book1", "author": "Author1"})
    with allure.step("Send GET request"):
        response = client.get("/books/")
    with allure.step("Verify response"):
        assert response.status_code == 200
        assert len(response.json()) == 1


@allure.feature("Books API")
@allure.story("Get Single Book")
def test_get_book():
    with allure.step("Create a book"):
        create_response = client.post(
            "/books/", json={"title": "Allure Book2", "author": "Author2"}
        )
        book_id = create_response.json()["id"]
    with allure.step("Send GET request for single book"):
        response = client.get(f"/books/{book_id}")
    with allure.step("Verify response"):
        assert response.status_code == 200
        assert response.json()["title"] == "Allure Book2"


@allure.feature("Books API")
@allure.story("Update Book")
def test_update_book():
    with allure.step("Create a book"):
        create_response = client.post(
            "/books/", json={"title": "Allure Book3", "author": "Author3"}
        )
        book_id = create_response.json()["id"]
    with allure.step("Send PUT request to update"):
        response = client.put(
            f"/books/{book_id}", json={"title": "Updated Allure Title"}
        )
    with allure.step("Verify response"):
        assert response.status_code == 200
        assert response.json()["title"] == "Updated Allure Title"


@allure.feature("Books API")
@allure.story("Delete Book")
def test_delete_book():
    with allure.step("Create a book"):
        create_response = client.post(
            "/books/", json={"title": "Allure Book4", "author": "Author4"}
        )
        book_id = create_response.json()["id"]
    with allure.step("Send DELETE request"):
        response = client.delete(f"/books/{book_id}")
    with allure.step("Verify deletion"):
        assert response.status_code == 200
        get_response = client.get(f"/books/{book_id}")
        assert get_response.status_code == 404
