import psycopg2 as db


class Database:
    def __init__(self, db_name):
        self.database_name = db_name
        self.cursor = None
        self.connection = None

    def __enter__(self):
        self.connection = db.connect(
            host='localhost',
            user='postgres',
            password='password4u3i2ndkf',
            database=self.database_name,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"Error occur {exc_value}")
            self.connection.rollback()
        else:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()


def insert_user(user_obj):
    with Database('library_db') as cursor:
        query = 'INSERT INTO users (user_name,user_password, user_email) VALUES (%s, %s, %s)'
        cursor.execute(query, (user_obj.name, user_obj.password, user_obj.email))


def insert_book(book_name):
    with Database('library_db') as cursor:
        query = 'INSERT INTO books (books_name) VALUES (%s)'
        cursor.execute(query, book_name)


def get_all_books():
    with Database('library_db') as cursor:
        query = 'SELECT book_name ' 'FROM books'
        cursor.execute(query)
        print(cursor.fetchall())


def get_all_authors():
    with Database('library_db') as cursor:
        query = 'SELECT *' 'FROM author'
        cursor.execute(query)
        print(cursor.fetchall())


def get_all_users():
    with Database('library_db') as cursor:
        query = 'SELECT * ' 'FROM users'
        cursor.execute(query)
        print(cursor.fetchall())


def get_author_book():
    with Database('library_db') as cursor:
        query = (
            'SELECT author.first_name, author.last_name, books.book_name '
            'FROM author '
            'INNER JOIN books '
            'ON author.author_id = books.author_id'
        )
        cursor.execute(query)
        print(cursor.fetchall())


def search_book(book_name):
    with Database('library_db') as cursor:
        query = 'SELECT * FROM books WHERE books.book_name = %s'
        cursor.execute(query, (book_name,))
        print(cursor.fetchall())


def borrow_book(user_obj, book_obj):
    with Database('library_db') as cursor:
        query1 = 'SELECT book_id FROM books WHERE book_name = %s'
        cursor.execute(query1, (book_obj.name,))
        book_id = cursor.fetchone()
        # add checking
        query2 = 'SELECT user_id FROM users WHERE user_name = %s AND user_email = %s'
        cursor.execute(query2, (user_obj.name, user_obj.email))
        user_id = cursor.fetchone()
        # checking
        query3 = 'INSERT INTO loans (book_id,user_id) VALUES (%s, %s)'
        cursor.execute(query3, (book_id, user_id))


if __name__ == '__main__':
    get_all_authors()
