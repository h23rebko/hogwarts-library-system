from src.book_service import BookService
from src.library_repository import LibraryRepository
import pytest

# Test som kollar att bok läggs till korrekt
def test_add_book_adds_book_to_repository():
    repo = LibraryRepository()
    service = BookService(repo)

    service.add_book("Hogwarts: En historia")

    assert "Hogwarts: En historia" in repo.available_books

# Kollar så att strängen inte är tom vid ny bok
def test_add_book_raises_error_if_title_empty():
    repo = LibraryRepository()
    service = BookService(repo)

    with pytest.raises(ValueError):
        service.add_book("")

# Test som kollar så att listan över tillgängliga böcker uppdateras korrekt
def test_get_available_books_returns_correct_list():
    repo = LibraryRepository()
    service = BookService(repo)

    service.add_book("Testbok")

    books = service.get_available_books()

    assert books == ["Testbok"]

# Kollar så att strängen med bara mellanslag inte godkänns
def test_add_book_raises_error_if_title_only_contains_spaces():
    repo = LibraryRepository()
    service = BookService(repo)

    with pytest.raises(ValueError, match="Book title cannot be empty"):
        service.add_book("   ")


# Test som kollar att mellanslag i början och slutet tas bort när en bok läggs till
def test_add_book_strips_whitespace_before_adding():
    repo = LibraryRepository()
    service = BookService(repo)

    service.add_book("  Testbok  ")

    assert "Testbok" in repo.available_books


# Test som kollar att book_exists returnerar True om boken finns, oavsett stora/små bokstäver
def test_book_exists_returns_true_for_existing_book_case_insensitive():
    repo = LibraryRepository()
    service = BookService(repo)

    service.add_book("Hogwarts: En historia")

    assert service.book_exists("hogwarts: en historia") is True


# Test som kollar att book_exists returnerar False om boken inte finns
def test_book_exists_returns_false_for_missing_book():
    repo = LibraryRepository()
    service = BookService(repo)

    service.add_book("Hogwarts: En historia")

    assert service.book_exists("Okänd bok") is False


# Test som kollar att find_available_book hittar rätt bok oavsett stora/små bokstäver
def test_find_available_book_returns_correct_book_case_insensitive():
    repo = LibraryRepository()
    service = BookService(repo)

    service.add_book("Hogwarts: En historia")
    service.add_book("Avancerade Trolldrycker")

    assert service.find_available_book("hogwarts: en historia") == "Hogwarts: En historia"
    assert service.find_available_book("AVANCERADE TROLLDRYCKER") == "Avancerade Trolldrycker"


# Test som kollar att find_available_book returnerar None om boken inte finns
def test_find_available_book_returns_none_if_book_not_found():
    repo = LibraryRepository()
    service = BookService(repo)

    service.add_book("Hogwarts: En historia")

    assert service.find_available_book("Finns inte") is None
