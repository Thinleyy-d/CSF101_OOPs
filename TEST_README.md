## OVERVIEW
This readme provides a detail description of the unit tests i created for the Library Management System, including the resources utilized, justifications for their use, and relevant information regarding the testing framework and methodology.

## RESOURCES USED
1. Python Programming language
2. unittest Framework
   -unittest is a built-in Python module that provides a framework for creating and running tests.
3. Object-Oriented Programming (OOP) Principles
   -OOP is a programming paradigm that uses "objects" to represent data and methods to manipulate that data.

## Test Cases Overview
-Adding Books: Verifying that an admin can successfully add a book to the library.
-Borrowing Books: Testing that users can borrow available books and that the system correctly handles attempts to borrow already borrowed books.
-Returning Books: Ensuring that users can return borrowed books and that the system updates the book's availability status accordingly.
-Viewing Available and Borrowed Books: Checking that the system accurately gives the available and borrowed books.

## Test Case Details
-Test Class: TestLibraryManagementSystem
Setup Method: Initializes a Library object and adds a few Book objects. It also creates User and Admin objects for testing.
-Test Methods:
 test_add_book: Tests the ability of an admin to add a book.
 test_borrow_book_success: Validates successful borrowing of an available book.
 test_borrow_book_not_available: Ensures that a user cannot borrow a book that is already borrowed.
 test_return_book_success: Confirms that a user can return a borrowed book.
 test_return_book_not_borrowed: Tests the behavior when attempting to return a book that was never borrowed.
 test_view_available_books: Checks that available books are correctly displayed.
 test_view_borrowed_books: Validates that borrowed books are accurately reflected.

## Conclusion
-The unit tests for the Library Management System provide a comprehensive validation of its functionalities, ensuring that each component operates as intended. The use of Python and the unittest framework allows for efficient testing, while the application of OOP principles facilitates clear organization and maintainability of the codebase. This documentation serves as a guide for understanding the testing methodology and resources utilized in the development of the test cases.