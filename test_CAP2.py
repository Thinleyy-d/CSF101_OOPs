import unittest
from CSF101_CAP2_02230308 import Library, Book, User, Admin

class TestLibraryManagementSystem(unittest.TestCase):

    def setUp(self):
        # Setting up a library and some books for testing
        self.library = Library()
        self.book1 = Book("To Kill a Mocking Bird", "Harper Lee")
        self.book2 = Book("Brave New World", "Aldous Huxley")
        self.book3 = Book("The Alchemist", "Paulo Coelho")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)

        self.user = User("Thinley Dorji")
        self.admin = Admin("Admin123")

    def test_add_book(self):
        # Test that an admin can add a book to the library
        self.admin.add_book(self.library, "Dawa Koto", "Dorji Gyeltshen")
        self.assertIn("Dawa Koto", [book.title for book in self.library.books])  # Checks if the book was added

    def test_borrow_book_success(self):
        # Test that a user can successfully borrow an available book
        self.user.borrow_book(self.library, "To Kill a Mocking Bird")
        self.assertFalse(self.book1.is_available)  # now the book is unavailable
        self.assertIn(self.book1, self.user.borrowed_books)  # The book should be in the user's borrowed list

    def test_borrow_book_not_available(self):
        # Test borrowing a book that is already borrowed
        self.user.borrow_book(self.library, "To Kill a Mocking Bird")  # First borrow
        self.user.borrow_book(self.library, "To Kill a Mocking Bird")  # Try to borrow again
        self.assertEqual(len(self.user.borrowed_books), 1)  # User should still have only one book

    def test_return_book_success(self):
        # Test that a user can successfully return a borrowed book
        self.user.borrow_book(self.library, "To Kill a Mocking Bird")  # Borrow the book
        self.user.return_book(self.library, "To Kill a Mocking Bird")  # Return the book
        self.assertTrue(self.book1.is_available)  # now the book is available
        self.assertNotIn(self.book1, self.user.borrowed_books)  # The book should not be in the user's borrowed list

    def test_return_book_not_borrowed(self):
        # Test returning a book that was never borrowed
        self.user.return_book(self.library, "To Kill a Mocking Bird")  # Try to return without borrowing
        self.assertTrue(self.book1.is_available)  # The book should still be available

    def test_view_available_books(self):
        # Test viewing available books in the library
        available_books = [book.title for book in self.library.books if book.is_available]
        self.assertIn("To Kill a Mocking Bird", available_books)  # Should be available for now
        self.user.borrow_book(self.library, "To Kill a Mocking Bird")  # Borrow the book
        available_books = [book.title for book in self.library.books if book.is_available]
        self.assertNotIn("To Kill a Mocking Bird", available_books)  # now it is unavailable

    def test_view_borrowed_books(self):
        # Test viewing borrowed books in the library
        self.user.borrow_book(self.library, "To Kill a Mocking Bird")  # Borrow the book
        borrowed_books = [book.title for book in self.library.books if not book.is_available]
        self.assertIn("To Kill a Mocking Bird", borrowed_books)  # Should be listed as borrowed

if __name__ == '__main__':
    unittest.main()  # Run the tests