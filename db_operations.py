import sqlite3


class DBOperations():
    """Database operations."""
    def __init__(self):
        """Init function."""
        try:
            self.conn = sqlite3.connect("weather.sqlite")
            self.c = self.conn.cursor()
        except Exception as e:
            print("Error opening DB:", e)

    # Work in progress.
    def fetch_data(self, sql):
        """Fetch data from the database."""
        try:
            self.c.execute(sql)
            return self.c.fetchall()
        except Exception as e:
            print("Error fetching data:", e)

    # Work in progress.
    def save_data(self, sql, data):
        """Save data to the database."""
        try:
            self.c.execute(sql, data)
            self.conn.commit()
        except Exception as e:
            print("Error saving data:", e)

    def initialize_db(self):
        """Initialize the database."""
        try:
            self.c.execute("""create table samples
                            (id integer primary key autoincrement not null,
                            sample_date text not null,
                            location text not null,
                            min_temp real not null,
                            max_temp real not null,
                            avg_temp real not null);""")
            self.conn.commit()
            print("Table created successfully.")
        except Exception as e:
            print("Error creating table:", e)

    def purge_data(self):
        """Purge data from the database."""
        try:
            self.c.execute("delete from samples")
            self.conn.commit()
            print("Data purged successfully.")
        except Exception as e:
            print("Error purging data:", e)
