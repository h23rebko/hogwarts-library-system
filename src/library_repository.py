class LibraryRepository:
    def __init__(self):
        self.available_books = []
        self.loaned_books = []
        self.loan_history = []

    # ---- BIBLIOTEK ----
    def add_book(self, title):
        self.available_books.append(title)

    def remove_available_book(self, title):
        self.available_books.remove(title)

    def add_loaned_book(self, title):
        self.loaned_books.append(title)

    def remove_loaned_book(self, title):
        self.loaned_books.remove(title)

    # ---- HISTORIK ----
    def add_to_history(self, title):
        self.loan_history.append(title)