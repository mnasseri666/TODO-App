from customtkinter import *

from todo_app.database.check_box_db import CheckBoxDb
from todo_app.database.tasks_database import TasksDatabase
from todo_app.paths import get_database_path


class DashboardTopLevel(CTkToplevel):
    def __init__(self, *args, username: str, main_app, **kwargs):
        super().__init__(*args, **kwargs)

        self.main_app = main_app

        self.title("Dashboard")
        self.geometry("650x500")

        self.__db = TasksDatabase(
            get_database_path(),
            username,
        )

        self.__db_checkbox = CheckBoxDb(
            get_database_path(),
            username,
        )

        self.checked_or_not = [
            _[3] for _ in self.__db_checkbox.read_all() if _[2] == username
        ]

        # column configure
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # row configure
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.log_out_btn = CTkButton(
            self,
            text="logout",
            command=self.log_out,
        )
        self.log_out_btn.grid(
            row=0,
            column=2,
            sticky="ne",
            padx=10,
            pady=10,
        )

        self.title_frame = CTkFrame(
            self,
            corner_radius=25,
        )
        self.title_frame.grid(
            row=0,
            column=1,
            sticky="n",
        )

        self.title_lbl = CTkLabel(
            self.title_frame,
            text="Dashboard",
        )
        self.title_lbl.grid(
            row=0,
            column=0,
            pady=10,
            padx=20,
        )

        self.username_lbl = CTkLabel(
            self,
            text=f"user: {username}",
            font=CTkFont(weight="bold"),
        )
        self.username_lbl.grid(
            row=0,
            column=0,
            sticky="nw",
            pady=10,
            padx=10,
        )

        self.finished_tasks = CTkFrame(
            self,
            corner_radius=25,
        )
        self.finished_tasks.grid(
            row=1,
            column=0,
            sticky="sew",
            padx=7,
            pady=(0, 10),
        )

        self.checked = len([_ for _ in self.checked_or_not if _ == 1])

        self.make_lbl(
            self.finished_tasks,
            "Finished Tasks",
            self.checked,
        )

        self.total_task = CTkFrame(
            self,
            corner_radius=25,
        )
        self.total_task.grid(
            row=1,
            column=1,
            sticky="sew",
            padx=7,
            pady=(0, 10),
        )

        self.total_tasks_values = self.__db_checkbox.read_all()

        self.total_user_tasks = [_ for _ in self.total_tasks_values if _[2] == username]

        self.make_lbl(
            self.total_task,
            "Total Tasks",
            len(self.total_user_tasks),
        )

        self.unfinished_tasks = CTkFrame(
            self,
            corner_radius=25,
        )
        self.unfinished_tasks.grid(
            row=1,
            column=2,
            sticky="sew",
            padx=7,
            pady=(0, 10),
        )

        self.unchecked = len([_ for _ in self.checked_or_not if _ == 0])

        self.make_lbl(
            self.unfinished_tasks,
            "Unfinished Tasks",
            self.unchecked,
        )

    def make_lbl(
        self,
        president: CTkFrame,
        title: str,
        values: int | None = None,
    ):
        title_lbl = CTkLabel(
            president,
            text=title,
        )
        title_lbl.pack()

        if values is None:
            value_lbl = CTkLabel(
                president,
                text="it's don't work cause beta",
            )
        else:
            value_lbl = CTkLabel(
                president,
                text=values,
            )

        value_lbl.pack()

    def log_out(self):
        self.destroy()
        self.main_app.destroy()
        self.main_app.login_root.deiconify()
