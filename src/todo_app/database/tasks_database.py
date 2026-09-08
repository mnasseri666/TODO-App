from sqlite3 import connect


class TasksDatabase:

    def __init__(
        self,
        filename: str = "database.db",
        username: str | None = None,
    ):
        self.filename = filename
        self.username = username

        with connect(self.filename) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS task (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username NVARCHAR(30),
                    text NVARCHAR(30) NOT NULL,
                    about_text NVARCHAR(100)
                );
            """)

    def add(self, text, about_text, username):
        with connect(self.filename, timeout=10) as conn:
            conn.execute(
                """
                INSERT INTO task(text, about_text, username)
                VALUES (?, ?, ?)
                """,
                (text, about_text, username),
            )

    def remove(self, task_id):
        with connect(self.filename, timeout=10) as conn:
            conn.execute(
                "DELETE FROM task WHERE id = ?",
                (task_id,),
            )

    def read_all(self):
        with connect(self.filename) as conn:
            cursor = conn.execute("SELECT * FROM task")
            return cursor.fetchall()

    def get_text_by_id(self, task_id):
        with connect(self.filename) as conn:
            cursor = conn.execute(
                "SELECT text FROM task WHERE id = ?",
                (task_id,),
            )
            return cursor.fetchone()

    def edit_column(self, task_id, text, about_text):
        with connect(self.filename, timeout=10) as conn:
            conn.execute(
                """
                UPDATE task
                SET text = ?, about_text = ?
                WHERE id = ?
                """,
                (text, about_text, task_id),
            )

    def read_user_tasks(self):
        if not self.username:
            return []

        with connect(self.filename) as conn:
            cursor = conn.execute(
                "SELECT * FROM task WHERE username = ?",
                (self.username,),
            )
            return cursor.fetchall()