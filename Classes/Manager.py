from Classes.Book import *
from Classes.User import *

class Manager:
    def __init__(self):
        self.books = [] # for books
        self.users = {} # user object as a key

    def add_book(self,book_name,quantity):
        for book in self.books:
            if book.name == book_name:
                return "Book with this name already exist in library, quantity changed"
        book_obj = Book(book_name,quantity)
        self.books.append(book_obj)

    def add_user(self,user_name,user_id):
        for user in self.users:
            if user.id == user_id:
                return "User with this id already exist in library"
        else:
            user_object = User(user_name,user_id)
            self.users[user_object] = self.users.get(user_object)

    def search_book(self,book_name):
        for book in self.books:
            if book.name == book_name:
                return book
        print("No book with this name in library")

    def borrow_book(self,user_id,book_name):
        for user in self.users:
            if user.user_id == user_id:
                for book in self.books:
                    if book.name == book_name:
                        self.users[user] = book_name
                        return book
        return None

    def print_all_users(self):
        for user in self.users: # iterating through class object because class obj is key
            print(f"{user.name} {user.id}")

    def print_all_books(self):
        for index,book in enumerate(self.books):
            print(f"{index+1}. {book.name}")

