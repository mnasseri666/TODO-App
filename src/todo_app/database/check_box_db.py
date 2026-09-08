import sqlite3 as sql


class CheckBoxDb:
    def __init__(
        self,
        filename: str,
        username: str,
        task_id: int | None = None,
    ):
        self.username = username
        self.task_id = task_id
        self.filename = filename

        with sql.connect(self.filename) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS checkbox_status (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_id INT NOT NULL UNIQUE,
                    username NVARCHAR(30) NOT NULL,
                    finished INT
                );
                """
            )

            try:
                conn.execute(
                    """
                    INSERT INTO checkbox_status(
                        task_id,
                        username,
                        finished
                    )
                    VALUES (?, ?, ?)
                    """,
                    (task_id, username, 0),
                )
            except sql.IntegrityError:
                pass

    def read_user_finished(self):
        with sql.connect(self.filename) as conn:
            cursor = conn.execute(
                """
                SELECT *
                FROM checkbox_status
                WHERE username = ? AND task_id = ?
                """,
                (self.username, self.task_id),
            )
            return cursor.fetchall()

    def add_checked(self, task_id):
        with sql.connect(self.filename) as conn:
            conn.execute(
                """
                UPDATE checkbox_status
                SET finished = 1
                WHERE task_id = ?
                """,
                (task_id,),
            )

    def remove_checked(self, task_id):
        with sql.connect(self.filename) as conn:
            conn.execute(
                """
                UPDATE checkbox_status
                SET finished = 0
                WHERE task_id = ?
                """,
                (task_id,),
            )

    def read_all(self):
        with sql.connect(self.filename) as conn:
            cursor = conn.execute(
                "SELECT * FROM checkbox_status"
            )
            return cursor.fetchall()