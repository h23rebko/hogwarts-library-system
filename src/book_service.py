class BookService:
    def __init__(self, repository):
        self.repository = repository

    def add_book(self, title):
        title = title.strip()
        if not title:
            raise ValueError("Book title cannot be empty")

        self.repository.add_book(title)

    def get_available_books(self):
        return self.repository.available_books

    def book_exists(self, title):
        normalized = title.strip().lower()
        return any(book.lower() == normalized for book in self.repository.available_books)
    
    def find_available_book(self, title):
        normalized = title.strip().lower()
        for book in self.repository.available_books:
            if book.lower() == normalized:
                return book
        return None