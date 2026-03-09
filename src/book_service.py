class BookService:
    def __init__(self, repository):
        self.repository = repository

    def add_book(self, title):
        self.repository.add(title)
