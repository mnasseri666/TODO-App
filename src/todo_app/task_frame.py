from customtkinter import *

from todo_app.all_about_task import AllAboutTask
from todo_app.database.check_box_db import CheckBoxDb
from todo_app.database.tasks_database import TasksDatabase
from todo_app.paths import get_database_path


class TaskFrame(CTkFrame):
    def __init__(
        self,
        master,
        task_id,
        task_text,
        about_task,
        show_task_frame_instance,
        on_remove_task,
        username,
        *args,
        **kwargs,
    ):
        super().__init__(master, *args, **kwargs)

        self.__db = TasksDatabase(get_database_path())

        self.task_id = task_id
        self.task_text = task_text
        self.about_task = about_task
        self.on_remove_task = on_remove_task
        self.show_task_frame = show_task_frame_instance
        self.username = username

        self.__db_checkbox = CheckBoxDb(get_database_path(), username, task_id)

        # column configure
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)

        self.check_box = CTkCheckBox(
            self, text="check", command=self.add_to_database_checked
        )
        self.check_box.grid(row=0, column=0)

        self.user_data = self.__db_checkbox.read_user_finished()

        self.all_data = self.__db_checkbox.read_all()

        for data in self.user_data:
            if data[3]:
                self.check_box.select()
            else:
                self.check_box.deselect()

        self.task_btn = CTkButton(
            self, text=self.task_text, command=self.open_about_task
        )
        self.task_btn.grid(row=0, column=1)

        self.delete_button = CTkButton(self, text="remove", command=self.remove_task)
        self.delete_button.grid(row=0, column=2, sticky="nsew", padx=10, pady=5)

        self.all_about_task_root = None

    def add_to_database_checked(self):
        if self.check_box.get():
            self.__db_checkbox.add_checked(self.task_id)

        else:
            self.__db_checkbox.remove_checked(self.task_id)

    def remove_task(self):
        self.__db_checkbox.delete_task(self.task_id)
        self.__db.remove(self.task_id)

        if self.on_remove_task:
            self.on_remove_task(self.task_id)

    def open_about_task(self):
        if (
            self.all_about_task_root is None
            or not self.all_about_task_root.winfo_exists()
        ):
            self.all_about_task_root = AllAboutTask(
                self.task_id, self.task_text, self.about_task, self.show_task_frame, self.username
            )

        else:
            self.all_about_task_root.focus_force()
            self.all_about_task_root.lift()
