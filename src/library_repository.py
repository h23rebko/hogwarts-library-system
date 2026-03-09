
class LibraryRepository:
    def __init__(self):
        self.books = []

    def add(self, title):
        self.books.append(title)