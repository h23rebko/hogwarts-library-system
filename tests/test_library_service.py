from unittest.mock import Mock
import pytest

from src.library_service import LibraryService
from src.library_repository import LibraryRepository
from src.book_service import BookService
from src.loan_service import LoanService

def test_borrow_book_calls_dependencies():
    mock_book_service = Mock()
    mock_loan_service = Mock()
    mock_book_service.repository = Mock()

    mock_book_service.find_available_book.return_value = "Testbok"

    library_service = LibraryService(mock_book_service, mock_loan_service)

    library_service.borrow_book("Testbok")

    mock_book_service.repository.remove_available_book.assert_called_once_with("Testbok")
    mock_loan_service.register_loan.assert_called_once_with("Testbok")

def test_return_book_raises_error_if_not_loaned():
    # 1. Setup mocks
    mock_book_service = Mock()
    mock_loan_service = Mock()
    
    # 2. Simulera att boken INTE hittas (match blir None)
    mock_loan_service.find_loaned_book.return_value = None
    
    service = LibraryService(mock_book_service, mock_loan_service)
    
    # 3. Detta triggar 'if not match'-raden och 'raise'-raden
    with pytest.raises(ValueError, match="Book is not currently loaned"):
        service.return_book("En bok som inte är utlånad")


def test_borrow_book_raises_error_if_not_found():
    mock_book_service = Mock()
    mock_loan_service = Mock()

    mock_book_service.find_available_book.return_value = None

    library_service = LibraryService(mock_book_service, mock_loan_service)

    with pytest.raises(ValueError):
        library_service.borrow_book("Okänd bok")


def test_borrow_and_return_book_integration():
    # Riktiga objekt
    repository = LibraryRepository()
    book_service = BookService(repository)
    loan_service = LoanService(repository)
    library_service = LibraryService(book_service, loan_service)

    # Lägg till bok
    book_service.add_book("Testbok")

    # Låna bok
    library_service.borrow_book("Testbok")

    # Kontrollera att den är utlånad
    assert "Testbok" in repository.loaned_books
    assert "Testbok" not in repository.available_books

    # Lämna tillbaka
    library_service.return_book("Testbok")

    # Kontrollera att den är tillbaka
    assert "Testbok" in repository.available_books
    assert "Testbok" not in repository.loaned_books