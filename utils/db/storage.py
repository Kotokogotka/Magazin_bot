from sqlite3 import connect


class DatabaseManager:

    def __init__(self, path):
        self.conn = connect(path)
        self.conn.execute('pragma foreigen_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()


    def create_table(self):
        self.query(
            'CREATE TABLE IF NOT EXISTS products (idx text, title text,'
            'body text, photo blob, price int, tag text')
        self.query(
            'CREATE TABLE IF NOT EXISTS orders (cid int, user_name text,'
            'user_address text, product text')
        self.query(
            'CREATE TABLE IF NOT EXISTS cart (cid int, idx text, quantity int')
        self.query(
            'CREATE TABLE IF NOT EXISTS categories (idx text, title text)')
        self.query(
            'CREATE TABLE IF NOT EXISTS questions (cid int, question text,')

    def query(self, arg, value=None):
        if value is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, value)
        self.conn.commit()

    def fetchone(self, arg, values=None):
        if values is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchone()

    def fetchall(self, args, values=None):
        if values is None:
            self.cur.execute(args)
        else:
            self.cur.execute(args, values)
        return self.cur.fetchall()

    def __del__(self):
        self.conn.close()