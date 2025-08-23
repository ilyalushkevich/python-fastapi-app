from fastapi import APIRouter, HTTPException
from typing import List
from src.schemas import BookCreate, BookUpdate, BookResponse
from src.crud import create_book, get_books, get_book, update_book, delete_book

router = APIRouter()


@router.post("/", response_model=BookResponse)
def create_book_endpoint(book: BookCreate):
    return create_book(book)


@router.get("/", response_model=List[BookResponse])
def get_books_endpoint():
    return get_books()


@router.get("/{book_id}", response_model=BookResponse)
def get_book_endpoint(book_id: int):
    book = get_book(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/{book_id}", response_model=BookResponse)
def update_book_endpoint(book_id: int, book: BookUpdate):
    updated_book = update_book(book_id, book)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book


@router.delete("/{book_id}")
def delete_book_endpoint(book_id: int):
    if not delete_book(book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}
