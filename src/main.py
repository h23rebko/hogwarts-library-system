from src.library_repository import LibraryRepository
from src.book_service import BookService
from src.loan_service import LoanService
from src.library_service import LibraryService


def print_menu():
    print("\n=== Hogwarts Library ===")
    print("1. Lägg till bok")
    print("2. Låna bok")
    print("3. Lämna tillbaka bok")
    print("4. Visa tillgängliga böcker")
    print("5. Visa lånehistorik")
    print("0. Avsluta")


def main():
    repository = LibraryRepository()
    book_service = BookService(repository)
    loan_service = LoanService(repository)
    library_service = LibraryService(book_service, loan_service)

    # Förifyllt biblioteket med några böcker
    book_service.add_book("Hogwarts: En historia")
    book_service.add_book("Avancerade trolldrycker")
    book_service.add_book("Den stora boken om trollkarlar")

    while True:
        print_menu()
        choice = input("Välj alternativ: ")

        if choice == "1":
            title = input("Ange boktitel: ").strip() #"Strip" tar bort extra whitespace och case-insensitive
            book_service.add_book(title)
            print("Bok tillagd.")


        elif choice == "2":
            title = input("Ange bok att låna: ")
            try:
                library_service.borrow_book(title)
                print("Bok utlånad.")
            except ValueError as e:
                print(f"Fel: {e}")

        elif choice == "3":
            title = input("Ange bok att lämna tillbaka: ")
            try:
                library_service.return_book(title)
                print("Bok återlämnad.")
            except ValueError as e:
                print(f"Fel: {e}")

        elif choice == "4":
            books = book_service.get_available_books()
            print("Tillgängliga böcker:")
            print()  # Lägger till tom rad innan resultatet
            for book in books:
                print(f"- {book}")

        elif choice == "5":
            history = loan_service.get_loan_history()
            print("Lånehistorik:")
            print()  # Lägger till tom rad innan resultatet

            for entry in history:
                print(f"- {entry}")

        elif choice == "0":
            print("Avslutar systemet...")
            break

        else:
            print("Ogiltigt val.")


if __name__ == "__main__":
    main()


    # Kör konsol med:
    # py -m src.main