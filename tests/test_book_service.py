from src.book_service import BookService
from src.library_repository import LibraryRepository

import pytest

from src.book_service import BookService
from src.library_repository import LibraryRepository
import pytest


def test_add_book_adds_book_to_repository():
    repo = LibraryRepository()
    service = BookService(repo)

    service.add_book("Hogwarts: En historia")

    assert "Hogwarts: En historia" in repo.available_books


def test_add_book_raises_error_if_title_empty():
    repo = LibraryRepository()
    service = BookService(repo)

    with pytest.raises(ValueError):
        service.add_book("")


def test_get_available_books_returns_correct_list():
    repo = LibraryRepository()
    service = BookService(repo)

    service.add_book("Testbok")

    books = service.get_available_books()

    assert books == ["Testbok"]

# Kör alla tester:
# py -m pytest
# Kör endast detta test: 
# py -m pytest tests/test_book_service.py