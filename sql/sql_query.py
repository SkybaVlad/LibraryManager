import psycopg2 as db


class Database:
    def __init__(self,db_name):
        self.database_name = db_name
        self.cursor = None
        self.connection = None

    def __enter__(self):
        self.connection = db.connect(host='localhost',
                                    user='postgres',
                                    password='password4u3i2ndkf',
                                    database=self.database_name)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self,exc_type,exc_value,traceback):
        if exc_type:
            print(f"Error occur {exc_value}")
            self.connection.rollback()
        else:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()


def get_all_books():
    with Database('library_db') as cursor:
        query = 'SELECT book_name FROM books'
        cursor.execute(query)
        print(cursor.fetchall())

def insert_book(book_name):
    with Database('library_db') as cursor:
        query = 'INSERT INTO books (book_name) VALUES (%s)'
        cursor.execute(query, book_name)

def get_author_book():
    with Database('library_db') as cursor:
        query = ('SELECT author.first_name, author.last_name, books.book_name '
                 'FROM author '
                 'INNER JOIN books '
                 'ON author.author_id = books.author_id')
        cursor.execute(query)
        print(cursor.fetchall())

if __name__ == '__main__':
    get_author_book()