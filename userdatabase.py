import sqlite3 as sql


class UserDatabase:
    def __init__(self, file_name):
        self.db_name = file_name
        self.connect = sql.connect(file_name)
        self.cursor = self.connect.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS user(
                            username NVARCHAR(50) UNIQUE NOT NULL PRIMARY KEY,
                            full_name NVARCHAR(50),
                            password NVARCHAR(50) NOT NULL
                               );
                            """)
        self.connect.commit()
        self.connect.close()

    def insert_to_user_db(self, username, full_name, password):
        self.connect = sql.connect(self.db_name)
        self.cursor = self.connect.cursor()

        self.cursor.execute(
            "INSERT INTO user VALUES (?, ?, ?)", (username, full_name, password)
        )
        self.connect.commit()
        self.connect.close()

    def get_user_by_username(self, username):
        self.connect = sql.connect(self.db_name)
        self.cursor = self.connect.cursor()
        self.cursor.execute("SELECT username FROM user WHERE username = ?", (username,))

        value = self.cursor.fetchone()
        return value

    def get_all_db(self):
        self.connect = sql.connect(self.db_name)
        self.cursor = self.connect.cursor()
        self.cursor.execute("SELECT * FROM user")

        values = self.cursor.fetchall()
        return values
