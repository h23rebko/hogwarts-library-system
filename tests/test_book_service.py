from src.book_service import BookService
from src.library_repository import LibraryRepository

def test_add_book_adds_book_to_repository():
    repo = LibraryRepository()
    service = BookService(repo)

    service.add_book("Hogwarts: A History")

    assert "Hogwarts: A History" in repo.books
