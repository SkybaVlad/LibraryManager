from Classes.Book import *
from Classes.User import *
from sql.sql_query import *


class Manager:
    def __init__(self):
        pass

    def add_book(self, book_obj):
        insert_book(book_obj.book_name)

    def add_user(self, user_obj):
        insert_user(user_obj)

    def search_book(self, book_obj):
        search_book(book_obj.book_name)

    def borrow_book(self, user_obj, book_obj):
        borrow_book(user_obj, book_obj)

    def print_all_users(self):
        get_all_users()

    def print_all_books(self):
        get_all_books()
