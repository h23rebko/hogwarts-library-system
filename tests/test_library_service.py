from unittest.mock import Mock
from src.library_service import LibraryService

class LibraryService:
    def __init__(self, book_service, loan_service):
        self.book_service = book_service
        self.loan_service = loan_service


    # Mockat test
    def test_borrow_book_calls_register_loan():
        # Skapa mockade beroenden
        mock_book_service = Mock()
        mock_loan_service = Mock()

        # Ställ in beteende
        mock_book_service.book_exists.return_value = True

        # Skapa SUT (System Under Test)
        library_service = LibraryService(mock_book_service, mock_loan_service)

        # Kör metoden
        library_service.borrow_book("Testbok")

        # Verifiera att beroende anropades
        mock_loan_service.register_loan.assert_called_once_with("Testbok")