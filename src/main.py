from library_service import LibraryService
from book_service import BookService
from loan_service import LoanService
from library_repository import LibraryRepository

def main():
    repository = LibraryRepository()
    book_service = BookService(repository)
    loan_service = LoanService(repository)
    library_service = LibraryService(book_service, loan_service)

    print("Welcome to Hogwarts Library")

if __name__ == "__main__":
    main()
