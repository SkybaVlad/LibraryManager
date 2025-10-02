import unittest
from Classes.Book import Book
from Classes.User import User
from Classes.Manager import Manager

class TestManager(unittest.TestCase):
    def test_valid_data(self):
        m = Manager()
        self.assertEqual(m.books, [])
        self.assertEqual(m.users, {})

    def test_add_book(self):
        m = Manager()
        book_obj = Book("HarryPotter",1)
        m.add_book(book_obj.name,book_obj.quantity)
        added_book = m.books[0]
        self.assertEqual(added_book.name,book_obj.name)
        self.assertEqual(added_book.quantity,book_obj.quantity)

    def test_add_two_dublicate(self):
        m = Manager()
        book_obj = Book("HarryPotter",1)
        m.add_book(book_obj.name,book_obj.quantity)
        book_obj = Book("HarryPotter",1)
        m.add_book(book_obj.name,book_obj.quantity)
        self.assertEqual(len(m.books),1)

    def test_add_user(self):
        m = Manager()
        user_obj = User("John",3)
        m.add_user(user_obj.name,user_obj.user_id)
        self.assertIn(user_obj,m.users)

    def test_add_user_value(self):
        m = Manager()
        user_obj = User("John",3)
        m.add_user(user_obj.name,user_obj.user_id)
        self.assertEqual(m.users[user_obj],None)