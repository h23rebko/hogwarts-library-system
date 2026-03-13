class LibraryService:
    def __init__(self, book_service, loan_service):
        self.book_service = book_service
        self.loan_service = loan_service

    def borrow_book(self, title):
        match = self.book_service.find_available_book(title)

        if not match:
            raise ValueError("Book does not exist or is already loaned")

        self.book_service.repository.remove_available_book(match)
        self.loan_service.register_loan(match)

    def return_book(self, title):
        match = self.loan_service.find_loaned_book(title)

        if not match:
            raise ValueError("Book is not currently loaned")

        self.loan_service.register_return(match)
        self.book_service.repository.add_book(match)