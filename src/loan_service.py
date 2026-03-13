class LoanService:
    def __init__(self, repository):
        self.repository = repository

    def register_loan(self, title):
        self.repository.add_loaned_book(title)
        self.repository.add_to_history(title)

    def register_return(self, title):
        self.repository.remove_loaned_book(title)

    def get_loan_history(self):
        return self.repository.loan_history

    def is_loaned(self, title):
        return title in self.repository.loaned_books
    def find_loaned_book(self, title):
        normalized = title.strip().lower()
        for book in self.repository.loaned_books:
            if book.lower() == normalized:
                return book
        return None