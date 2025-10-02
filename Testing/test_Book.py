import unittest
from Classes.Book import Book

class TestBook(unittest.TestCase):
    def init_book(self):
        book = Book("Harry Potter",1)
        self.assertEqual(book.name, "Harry Potter")
        self.assertEqual(book.quantity,1)