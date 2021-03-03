import unittest
from library import Book, Library


class TestLibrary(unittest.TestCase):
    """This class is responsible for
    testing the working of the Library class."""

    def test_add_book(self) -> None:
        # Create a Library and Book:
        library = Library()
        book = Book('Dune', 'Frank Herbert',
                    884, 7, False, 14.99, 14.99)
        library.add_book(book)
        # Assert that the Book was added to the Library Dictionary
        assert book.name in library._books.keys()
        assert library._books[book.name]['author'] == 'Frank Herbert'


if __name__ == '__main__':
    unittest.main()
