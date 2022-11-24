'''
Name: 
Program: Business Information Technology
Course: ADEV-3005 Programming in Python
Created: 2022-11-24
Updated: 2022-11-24

TODO - Context manager for database connections.

Final Project
 
@author Adam Huybers [ahuybers@academic.rrc.ca]
@version 1.0.0
'''
import sqlite3


class DBCM():
    """Database connection manager."""
    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self.conn = sqlite3.connect(self.db)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace):
        self.conn.commit()
        self.conn.close()
        self.cursor.close()