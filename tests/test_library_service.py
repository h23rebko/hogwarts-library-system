from unittest.mock import Mock
from src.library_service import LibraryService


def test_borrow_book_calls_register_loan():
    # Mockade beroenden
    mock_book_service = Mock()
    mock_loan_service = Mock()

    # Mocka repository som finns inuti book_service
    mock_book_service.repository = Mock()

    # Beteende
    mock_book_service.find_available_book.return_value = "Testbok"

    # System Under Test
    library_service = LibraryService(mock_book_service, mock_loan_service)

    # Kör metoden
    library_service.borrow_book("Testbok")

    # Verifiera att rätt metoder anropades
    mock_book_service.repository.remove_available_book.assert_called_once_with("Testbok")
    mock_loan_service.register_loan.assert_called_once_with("Testbok")


def test_borrow_book_raises_error_if_book_not_found():
    mock_book_service = Mock()
    mock_loan_service = Mock()

    mock_book_service.find_available_book.return_value = None

    library_service = LibraryService(mock_book_service, mock_loan_service)

    try:
        library_service.borrow_book("Okänd bok")
    except ValueError:
        assert True
    else:
        assert False


def test_return_book_calls_register_return_and_add_book():
    mock_book_service = Mock()
    mock_loan_service = Mock()

    mock_book_service.repository = Mock()

    mock_loan_service.find_loaned_book.return_value = "Testbok"

    library_service = LibraryService(mock_book_service, mock_loan_service)

    library_service.return_book("Testbok")

    mock_loan_service.register_return.assert_called_once_with("Testbok")
    mock_book_service.repository.add_book.assert_called_once_with("Testbok")


def test_return_book_raises_error_if_not_loaned():
    mock_book_service = Mock()
    mock_loan_service = Mock()

    mock_loan_service.find_loaned_book.return_value = None

    library_service = LibraryService(mock_book_service, mock_loan_service)

    try:
        library_service.return_book("Testbok")
    except ValueError:
        assert True
    else:
        assert False