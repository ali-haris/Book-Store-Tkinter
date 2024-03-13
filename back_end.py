import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect('books.db')
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def to_insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES(null,?,?,?,?)",
                        (title, author, year, isbn))
        self.conn.commit()

    def to_view(self):
        self.cur.execute("SELECT * FROM book")
        row = self.cur.fetchall()
        return row

    def to_search(self, title="", author="", year="", isbn=""):
        self.cur.execute(
            "SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        row = self.cur.fetchall()
        return row

    def to_delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def to_update(self, title, author, year, isbn, id):
        self.cur.execute(
            "UPDATE book SET title=?, author=?,year=?,isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()


# to_self.connect()


# to_delete(1)
# print(to_search(title='The iceland'))
# to_insert('The sea','Haris',2080,545234343)

# to_update('The Land', 'Haris Khan',2053,23434234,3)


# print(to_view())
