from pydantic import BaseModel
from typing import List, Optional


class Book(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None


books_db: List[Book] = []
