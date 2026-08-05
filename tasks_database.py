from sqlite3 import *


class TasksDatabase:
    def __init__(self, filename, username=None):
        self.filename = filename
        self.username = username

        self.connect = connect(self.filename)
        self.cursor = self.connect.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS task(
            id INTEGER  PRIMARY KEY AUTOINCREMENT,
            username NVARCHAR(30),
            text NVARCHAR(30) NOT NULL, 
            about_text NVARCHAR(100)
        );
        """)
        self.connect.commit()
        self.connect.close()

    def add(self, text, about_text, username):
        self.connect = connect(self.filename)
        self.cursor = self.connect.cursor()
        self.cursor.execute(
            "INSERT INTO task(text, about_text, username) VALUES (?, ?, ?)",
            (text, about_text, username),
        )
        self.connect.commit()
        self.connect.close()

    def remove(self, task_id):
        self.connect = connect(self.filename)
        self.cursor = self.connect.cursor()
        self.cursor.execute("DELETE FROM task WHERE id = ?", (task_id,))
        self.connect.commit()
        self.connect.close()

    def read_all(self):
        self.connect = connect(self.filename)
        self.cursor = self.connect.cursor()
        data_cursor = self.cursor.execute("SELECT * FROM task")
        all_data = data_cursor.fetchall()
        self.connect.close()
        return all_data

    def get_text_by_id(self, task_id):
        self.connect = connect(self.filename)
        self.cursor = self.connect.cursor()
        data = self.cursor.execute("SELECT text FROM task WHERE id = ?", (task_id,))
        self.connect.close()
        return data.fetchone()

    def edit_column(self, task_id, text, about_text):
        self.connect = connect(self.filename)
        self.cursor = self.connect.cursor()
        self.cursor.execute(
            """UPDATE task
         SET text = ?, about_text = ?
         WHERE id = ?""",
            (text, about_text, task_id),
        )
        self.connect.commit()
        self.connect.close()

    def read_user_tasks(self):
        if self.username:
            self.connect = connect(self.filename)
            self.cursor = self.connect.cursor()
            data_cursor = self.cursor.execute(
                "SELECT * FROM task WHERE username = ?", (self.username,)
            )
            data = data_cursor.fetchall()
            self.connect.close()
            return data
