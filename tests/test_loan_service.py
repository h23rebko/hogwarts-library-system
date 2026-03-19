from unittest.mock import Mock
from src.loan_service import LoanService
from src.library_repository import LibraryRepository # Importera för att kunna instansiera vid behov, även om vi mockar
import pytest

#en fixtur som sätter upp LoanService med mockad repository för varje test.
@pytest.fixture
def setup_service():
    mock_repository = Mock(spec=LibraryRepository)
    loan_service = LoanService(mock_repository)
    return loan_service, mock_repository


def test_register_loan_calls_repository_methods(setup_service):
    # ARRANGE
    loan_service, mock_repository = setup_service
    book_title = "Hogwarts: En historia"

    # ACT
    loan_service.register_loan(book_title)

    # ASSERT
    mock_repository.add_loaned_book.assert_called_once_with(book_title)
    mock_repository.add_to_history.assert_called_once_with(book_title)


def test_register_return_calls_repository_method(setup_service):
    # ARRANGE
    loan_service, mock_repository = setup_service
    book_title = "Hogwarts: En historia"

    # ACT
    loan_service.register_return(book_title)

    # ASSERT
    mock_repository.remove_loaned_book.assert_called_once_with(book_title)


def test_get_loan_history_returns_repository_history(setup_service):
    # ARRANGE
    loan_service, mock_repository = setup_service
    mock_repository.loan_history = ["Bok A", "Bok B"]

    # ACT
    history = loan_service.get_loan_history()

    # ASSERT
    assert history == ["Bok A", "Bok B"]


def test_is_loaned_returns_true_if_book_is_loaned(setup_service):
    # ARRANGE
    loan_service, mock_repository = setup_service
    mock_repository.loaned_books = ["Testbok", "Annan bok"]

    # ACT & ASSERT
    assert loan_service.is_loaned("Testbok")


def test_is_loaned_returns_false_if_book_is_not_loaned(setup_service):
    # ARRANGE
    loan_service, mock_repository = setup_service
    mock_repository.loaned_books = ["Annan bok"]

    # ACT & ASSERT
    assert loan_service.is_loaned("Testbok") is False


def test_find_loaned_book_returns_correct_book_case_insensitive(setup_service):
    # ARRANGE
    loan_service, mock_repository = setup_service
    mock_repository.loaned_books = ["Hogwarts: En historia", "Avancerade Trolldrycker"]

    # ACT & ASSERT
    assert loan_service.find_loaned_book("hogwarts: en historia") == "Hogwarts: En historia"
    assert loan_service.find_loaned_book("AVANCERADE TROLLDRYCKER") == "Avancerade Trolldrycker"


def test_find_loaned_book_returns_none_if_not_found(setup_service):
    # ARRANGE
    loan_service, mock_repository = setup_service
    mock_repository.loaned_books = ["Hogwarts: En historia"]

    # ACT & ASSERT
    assert loan_service.find_loaned_book("Finns inte") is None

# Integrationstest! Verifierar hela låne- och returcykeln
# genom att använda den riktiga LibraryRepository.
def test_loan_service_integration_loan_and_return_cycle():

    # ARRANGE: Skapa riktiga instanser av servicen och dess beroende
    repository = LibraryRepository()
    loan_service = LoanService(repository)
    book_title = "Quidditch Through the Ages"

    # ACT 1: Registrera ett lån
    loan_service.register_loan(book_title)

    # ASSERT 1: Verifiera status efter lån
    assert book_title in repository.loaned_books
    assert book_title in repository.loan_history
    assert len(repository.loaned_books) == 1

    # ACT 2: Registrera en retur
    loan_service.register_return(book_title)

    # ASSERT 2: Verifiera status efter retur
    assert book_title not in repository.loaned_books
    assert len(repository.loaned_books) == 0
