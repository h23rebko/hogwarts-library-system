class BookService:
    def __init__(self, repository):
        self.repository = repository

    def add_book(self, title):
        if not title:
            raise ValueError("Book title cannot be empty")

        self.repository.add_book(title)

    def get_available_books(self):
        return self.repository.available_books

    def book_exists(self, title):
        return title in self.repository.available_books