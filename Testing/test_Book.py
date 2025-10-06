import unittest
from Classes.Book import Book

class TestBook(unittest.TestCase):
    def init_book(self):
        book = Book("Harry Potter")
        self.assertEqual(book.name, "Harry Potter")