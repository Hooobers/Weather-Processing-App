import sqlite3

class DBCM():
    """Database connection manager."""
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self):
        self.conn.commit()
        self.conn.close()