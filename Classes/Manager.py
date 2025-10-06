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
        for user in self.users:
            if user.user_id == user_id:
                for book in self.books:
                    if book.name == book_name:
                        self.users[user] = book_name
                        return book
        return None

    def print_all_users(self):
        get_all_users()

    def print_all_books(self):
        pass
