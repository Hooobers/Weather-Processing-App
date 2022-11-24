'''
Name: 
Program: Business Information Technology
Course: ADEV-3005 Programming in Python
Created: 2022-11-20
Updated: 2022-11-24

TODO - All database operations.

Final Project
 
@author Adam Huybers [ahuybers@academic.rrc.ca]
@version 1.0.3
'''
from dbcm import DBCM


class DBOperations():
    """Database operations."""
    def __init__(self, db):
        """Init function."""
        self.db = db

    def fetch_data(self, first, last, month):
        """Fetch data from the database."""
        try:
            # Context manager used to handle connections.
            with DBCM(self.db) as cm_cursor:
                if month:
                    first_date = first + '-01'
                    last_date = last + '-31'
                else:
                    first_date = first
                    last_date = last

                # Command execution.    
                cm_cursor.execute(f"select sample_date, avg_temp from samples where sample_date between '{first_date}' and '{last_date}' order by date(sample_date)")
                return [dict(row) for row in cm_cursor.fetchall()]

        except Exception as e:
            print("Error fetching data:", e)

    def save_data(self, data, month, year):
        """Save data to the database."""
        try:
            command = """insert into samples (sample_date, location, max_temp, min_temp, avg_temp)values (?,?,?,?,?)"""

            for day, temps in data.items():
                try:
                    set_data = list()
                    set_data.append(f"{year}-{month}-{day}")
                    set_data.append("Winnipeg")

                    for key, value in temps.items():
                        set_data.append(value)

                    with DBCM(self.db) as cm_cursor:
                        cm_cursor.execute(command, set_data)

                except Exception as e:
                    print("Error saving data:", e)
        except Exception as e:
            print("Error saving data:", e)

    def initialize_db(self):
        """Initialize the database."""
        try:
            # Context manager used to handle connections.
            with DBCM(self.db) as cm_cursor:
                cm_cursor.execute("""create table if not exists samples
                                 (id integer primary key autoincrement not null,
                                  sample_date text not null,
                                  location text not null,
                                  min_temp real not null,
                                  max_temp real not null,
                                  avg_temp real not null);""")
            print("Table created successfully.")
        except Exception as e:
            print("Error creating table:", e)

    def purge_data(self):
        """Purge data from the database."""
        try:
            # Context manager used to handle connections.
            with DBCM(self.db) as cm_cursor:
                cm_cursor.execute("delete from samples")
            print("Data purged successfully.")
        except Exception as e:
            print("Error purging data:", e)
