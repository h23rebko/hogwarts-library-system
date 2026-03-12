class LibraryService:
    def __init__(self, book_service, loan_service):
        self.book_service = book_service
        self.loan_service = loan_service

    def borrow_book(self, title):
        if not self.book_service.book_exists(title):
            raise ValueError("Book does not exist or is already loaned")

        # Ta bort från tillgängliga
        self.book_service.repository.remove_available_book(title)

        # Registrera lån
        self.loan_service.register_loan(title)

    def return_book(self, title):
        if not self.loan_service.is_loaned(title):
            raise ValueError("Book is not currently loaned")

        # Ta bort från loaned
        self.loan_service.register_return(title)

        # Lägg tillbaka till available
        self.book_service.repository.add_book(title)