import sqlite3

class DatabaseHandler:
    def __init__(self, db_name='myapp.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        # Create the Users table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )''')

        # Create the Notes table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            note_text TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )''')

        # Create the Roles table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS roles (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            role TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )''')

        self.conn.commit()

    def close_connection(self):
        self.conn.close()

    



if __name__ == "__main__":
    db_handler = DatabaseHandler()
    db_handler.create_tables()
    db_handler.close_connection()


