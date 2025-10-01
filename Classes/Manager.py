from Book import *
from User import *

class Manager:
    def __init__(self):
        self.books = []
        self.users = {} # for borrow

    def print_all_books(self):
        for index,book in enumerate(self.books):
            print(f"{index+1}. {book.name}")


