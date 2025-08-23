from typing import List, Optional
from src.models import Book, books_db
from src.schemas import BookCreate, BookUpdate


def get_next_id() -> int:
    return len(books_db) + 1


def create_book(book: BookCreate) -> Book:
    new_book = Book(id=get_next_id(), **book.model_dump())
    books_db.append(new_book)
    return new_book


def get_books() -> List[Book]:
    return books_db


def get_book(book_id: int) -> Optional[Book]:
    for book in books_db:
        if book.id == book_id:
            return book
    return None


def update_book(book_id: int, book_update: BookUpdate) -> Optional[Book]:
    for book in books_db:
        if book.id == book_id:
            if book_update.title is not None:
                book.title = book_update.title
            if book_update.author is not None:
                book.author = book_update.author
            if book_update.description is not None:
                book.description = book_update.description
            return book
    return None


def delete_book(book_id: int) -> bool:
    for i, book in enumerate(books_db):
        if book.id == book_id:
            del books_db[i]
            return True
    return False
