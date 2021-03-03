from typing import Dict, List, Callable
import json


class Book:
    """A book is a medium for recording information in the form
    of writing or images, typically composed of many pages (made of
    papyrus, parchment, vellum, or paper) bound together
    and protected by cover.

    === Public Attributes ===
    name: A string representing the book title.
    author: A string representing the author's name.
    pages: The length of the book as a positive integer.
    condition: The condition of the book as an integer
               from 1 to 5.
    read: A boolean value representing if the book has
          been read or not.
    price: The first found price on the internet.
    paid: If available, the prince initially paid.
    """

    name: str
    author: str
    pages: int
    condition: int
    read: bool
    price: float
    paid: float

    def __init__(self, name: str, author: str,
                 pages: int, condition: int, read: bool,
                 price: float, paid: float) -> None:
        self.name = name
        self.author = author
        self.pages = pages
        self.condition = condition
        self.read = read
        self.price = price
        self.paid = paid


class Library:
    """A Library is a collection of Books, both Non-fiction and
    Fiction, that can be sorted in a multitude of ways. This class
    includes sorting algorithms, and data storage.

    === Private Attributes ===
    _books: A dictionary with format {'<book_name>': <data>}
            where <data> is a dictionary containing book attributes.
    """
    _books: Dict

    def __init__(self) -> None:
        self._books = {}

    def add_book(self, book: Book) -> None:
        """If entry does not exist for Book, introduce entry
        into <self._books>. If entry does exist, update the
        entry accordingly.
        """

        books = self._books
        books.update({book.name: {'author': book.author,
                                  'pages': book.pages,
                                  'condition': book.condition,
                                  'read': book.read,
                                  'price': book.price,
                                  'paid': book.paid}})

    def interactive_load(self) -> None:
        """Uses iterative add_book method to add books
        to <self._books>"""
        stop = False
        while not stop:
            name = input('Book Name :')
            author = input('Author Name: ')
            pages = int(input('Number of Pages: '))
            condition = int(input('Condition: '))
            finished = bool(input('Finished? (y or empty): '))
            price = float(input('Current Price: '))
            paid = float(input('Initial Payment: '))
            stop = bool(input('Stop? (y or empty): '))
            self.add_book(Book(name, author, pages, condition,
                               finished, price, paid))

    def sort(self, priority: Callable[[List[Book]], bool]) -> None:
        pass

    def export(self) -> None:
        """Exports to a file with the given <self._books>
        dictionary structure."""

        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(self._books, f, ensure_ascii=False, indent=4)

    def read_json(self) -> None:
        """Reads the file from <data.json> and updates
        <self._books> to include those previously preserved values.

        === Precondition ===
        The method _export has been called at least once before.
        Or, the file 'data.json' is not empty.
        """

        self._books = json.load(open('data.json', 'r'))


if __name__ == '__main__':
    import doctest
    import unittest
    import testing

    suite = unittest.TestLoader().loadTestsFromModule(testing)
    unittest.TextTestRunner(verbosity=2).run(suite)

    doctest.testmod()
