# book class
class Book:
    def __init__(self, title, author):
        self.title = title # title of the book
        self.author = author # author of the book
        self.is_available = True # indicates whether the book is available

    def __str__(self):# string representation for book object
        status = "Available" if self.is_available else "Unavailable"
        return f"Title: {self.title}, Author: {self.author}, Status: {status}" # returns updated string with book details and availability status
    
# user class
class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []# list to store borrowed books

    def borrow_book(self, library, book_title):# method to borrow the books
        for book in library.books:# goes through books in the library
            if book.title == book_title and book.is_available:
                book.is_available = False
                self.borrowed_books.append(book)
                print(f"{self.name} borrowed '{book.title}'.")
                return
        print(f"{book_title} is not available.")

    def return_book(self, library, book_title):# method to return the books
        for book in self.borrowed_books:# goes through borrowed book of user
            if book.title == book_title:
                book.is_available = True
                self.borrowed_books.remove(book)
                print(f"{self.name} returned '{book.title}'.")
                return
        print(f"{self.name} did not borrow '{book_title}'.")

# admin class
class Admin(User):# admin derived from user class
    def add_book(self, library, title, author):# method to add a book to the library
        new_book = Book(title, author)
        library.books.append(new_book)# add a new book to the library
        print(f"You {self.name} added '{title}' to the library.")

# library class
class Library:
    def __init__(self):
        self.books = []# list to store books in the library

    def add_book(self, book):
        self.books.append(book) # append the book to library list

    def view_books(self):# displays all the books in the library
        if not self.books:
            print("Books not available in the library.")
        else:
            for book in self.books:
                print(book)

    def view_available_books(self):# displays only available books
        available_books = [book for book in self.books if book.is_available]
        if not available_books:
            print("No available books for now.")
        else:
            for book in available_books:# goes through available books and prints them
                print(book)

    def view_borrowed_books(self):# displays only borrowed books
        borrowed_books = [book for book in self.books if not book.is_available]
        if not borrowed_books:
            print("No borrowed books.")
        else:
            for book in borrowed_books:# goes through borrowed books and prints them
                print(book)

# main program starts here
def main():# main function to run the program
    # initialize library
    library = Library()
    # added some books of my own
    library.add_book(Book("To Kill a Mocking Bird", "Harper Lee"))
    library.add_book(Book("Brave New World", "Aldous"))
    library.add_book(Book("The Alchemist", "Paulo Coelheo"))

    admin = Admin("Admin123")
    user = User("Thinley Dorji")

    print("Welcome to CST Library Management System!")

    while True:
        role = input("Are you an Admin or a User? (admin/user) Or type 'exit' to quit: ").lower()

        if role == "admin":
            password = input("Enter Admin password: ")
            if password == "Admin123":
                print("\n----------Accessing Admin----------")
                while True:
                    print("\nAdmin Menu:")
                    print("1. View all books")
                    print("2. Add a book")
                    print("3. Exit")
                    choice = input("Choose an option: ")

                    if choice == "1":
                        print("\nBooks in the Library:")
                        library.view_books()
                    elif choice == "2":
                        title = input("Enter book title: ")
                        author = input("Enter author name: ")
                        admin.add_book(library, title, author)
                    elif choice == "3":
                        break
                    else:
                        print("Invalid Choice. Try again.")
            else:
                print("Incorrect password.")
        elif role == "user":
            print("\n----------Accessing User----------")
            while True:
                print("\nUser Menu:")
                print("1. View available books")
                print("2. Borrow a book")
                print("3. Return a book")
                print("4. Exit")
                choice = input("Choose an option: ")

                if choice == "1":
                    print("\nAvailable Books:")
                    library.view_available_books()
                elif choice == "2":
                    book_title = input("Enter book title to borrow: ")
                    user.borrow_book(library, book_title)
                elif choice == "3":
                    book_title = input("Enter book title to return: ")
                    user.return_book(library, book_title)
                elif choice == "4":
                    break
                else:
                    print("Invalid choice. Try again.")
        elif role == "exit":
            print("Thank you for using my library system. ByeBye!!")
            break
        else:
            print("Invalid input. Please enter 'admin', 'user', or 'exit'.")

if __name__ == "__main__":
    main()
