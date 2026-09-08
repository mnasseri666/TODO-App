import sqlite3 as sql


class UserDatabase:
    def __init__(self, file_name: str = "database.db"):
        self.db_name = file_name

        with sql.connect(self.db_name) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS user (
                    username NVARCHAR(50) UNIQUE NOT NULL PRIMARY KEY,
                    full_name NVARCHAR(50),
                    password NVARCHAR(50) NOT NULL
                );
                """
            )

    def insert_to_user_db(
        self,
        username: str,
        full_name: str,
        password: str,
    ):
        with sql.connect(self.db_name) as conn:
            conn.execute(
                "INSERT INTO user VALUES (?, ?, ?)",
                (username, full_name, password),
            )

    def get_user_by_username(self, username: str):
        with sql.connect(self.db_name) as conn:
            cursor = conn.execute(
                "SELECT username FROM user WHERE username = ?",
                (username,),
            )

            return cursor.fetchone()

    def get_all_db(self):
        with sql.connect(self.db_name) as conn:
            cursor = conn.execute("SELECT * FROM user")

            return cursor.fetchall()
