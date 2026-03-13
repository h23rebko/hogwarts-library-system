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


def print_result(message):
    print("\n" + "=" * 30)
    print("RESULTAT")
    print("=" * 30)
    print()
    print(message)
    print("\n" + "=" * 30)
    input("\nTryck Enter för att fortsätta...")


def main():
    repository = LibraryRepository()
    book_service = BookService(repository)
    loan_service = LoanService(repository)
    library_service = LibraryService(book_service, loan_service)

    # Förifyllt biblioteket med några böcker
    book_service.add_book("Hogwarts: En historia")
    book_service.add_book("Avancerade trolldrycker")
    book_service.add_book("Den stora boken om trollkarlar")
    book_service.add_book("Magiska varelser och vart man finner dem")
    book_service.add_book("De fyra elevhemmen")
    book_service.add_book("Hur man inte spränger sin kittel")

    while True:
        print_menu()
        choice = input("Välj alternativ: ")

        if choice == "1":
            title = input("Ange boktitel: ").strip() #"Strip" tar bort extra whitespace och case-insensitive
            book_service.add_book(title)
            print_result("Bok tillagd.")


        elif choice == "2":
            title = input("Ange bok att låna: ")
            try:
                library_service.borrow_book(title)
                print("Bok utlånad.")
            except ValueError as e:
                print_result(f"Fel: {e}")

        elif choice == "3":
            title = input("Ange bok att lämna tillbaka: ")
            try:
                library_service.return_book(title)
                print("Bok återlämnad.")
            except ValueError as e:
                print_result(f"Fel: {e}")
    
        elif choice == "4":
            books = book_service.get_available_books()

            if not books:
                print_result("Inga tillgängliga böcker.")
            else:
             formatted = "\n".join(f"- {book}" for book in books)
             print_result(f"Tillgängliga böcker:\n\n{formatted}")
                

        elif choice == "5":
            history = loan_service.get_loan_history()

            if not history:
                print_result("Ingen lånehistorik ännu.")
            else:
                formatted = "\n".join(f"- {entry}" for entry in history)
                print_result(f"Lånehistorik:\n\n{formatted}")

        elif choice == "0":
            print_result("Avslutar systemet...")
            break

        else:
            print_result("Ogiltigt val.")


if __name__ == "__main__":
    main()


    # Kör konsol med:
    # py -m src.main