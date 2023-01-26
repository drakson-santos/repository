import sqlite3
from databases import IDatabase

class SqlLiteDatabase(IDatabase):

    def __init__(self, database_name):
        self.conn = sqlite3.connect('database.sqlite')
        self.cursor = self.conn.cursor()
        self.create_table_if_not_exists(database_name)

    def create_table_if_not_exists(self, database_name):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (database_name,))
        if self.cursor.fetchone() is None:
            self.cursor.execute(f"CREATE TABLE {database_name} (id TEXT PRIMARY KEY, product_name TEXT)")
            self.conn.commit()

    def create(self, sql, params=None):
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.lastrowid

    def read(self, sql, params=None):
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update(self, sql, params=None):
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.rowcount

    def delete(self, sql, params=None):
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.rowcount