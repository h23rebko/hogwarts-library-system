
from unittest.mock import Mock
from src.loan_service import LoanService


def test_register_loan_calls_repository_methods():
    mock_repository = Mock()
    loan_service = LoanService(mock_repository)

    loan_service.register_loan("Testbok")

    mock_repository.add_loaned_book.assert_called_once_with("Testbok")
    mock_repository.add_to_history.assert_called_once_with("Testbok")


def test_register_return_calls_remove():
    mock_repository = Mock()
    loan_service = LoanService(mock_repository)

    loan_service.register_return("Testbok")

    mock_repository.remove_loaned_book.assert_called_once_with("Testbok")


def test_find_loaned_book_case_insensitive():
    mock_repository = Mock()
    mock_repository.loaned_books = ["Testbok"]

    loan_service = LoanService(mock_repository)

    result = loan_service.find_loaned_book(" testbok ")

    assert result == "Testbok"


def test_find_loaned_book_returns_none_if_not_found():
    mock_repository = Mock()
    mock_repository.loaned_books = ["Testbok"]

    loan_service = LoanService(mock_repository)

    result = loan_service.find_loaned_book("Another book")

    assert result is None