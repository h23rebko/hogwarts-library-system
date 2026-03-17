from src.library_repository import LibraryRepository
import pytest

@pytest.fixture
def repo():
    return LibraryRepository()

def test_add_book_adds_book_to_available_books(repo):
    repo.add_book("Hogwarts: En historia")

    assert "Hogwarts: En historia" in repo.available_books

def test_remove_available_book_removes_existing_book_from_available_books(repo):
    repo.add_book("Hogwarts: En historia")
    repo.remove_available_book("Hogwarts: En historia")

    assert "Hogwarts: En historia" not in repo.available_books

def test_remove_available_book_raises_error_if_not_found(repo):
    with pytest.raises(ValueError):
        repo.remove_available_book("Nonexistent book")

def test_add_loaned_book_adds_book_to_loaned_books(repo):
    repo.add_loaned_book("Hogwarts: En historia")

    assert "Hogwarts: En historia" in repo.loaned_books

def test_remove_loaned_book_removes_existing_book_from_loaned_books(repo):
    repo.add_loaned_book("Hogwarts: En historia")
    repo.remove_loaned_book("Hogwarts: En historia")

    assert "Hogwarts: En historia" not in repo.loaned_books

def test_remove_loaned_book_raises_error_if_not_found(repo):
    with pytest.raises(ValueError):
        repo.remove_loaned_book("Nonexistent book")

def test_add_to_history_adds_book_to_loan_history(repo):
    repo.add_to_history("Hogwarts: En historia")

    assert "Hogwarts: En historia" in repo.loan_history