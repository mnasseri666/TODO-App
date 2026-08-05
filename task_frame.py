from customtkinter import *

from all_about_task import AllAboutTask
from tasks_database import TasksDatabase


class TaskFrame(CTkFrame):
    def __init__(
        self,
        master,
        task_id,
        task_text,
        about_task,
        show_task_frame_instance,
        on_remove_task,
        *args,
        **kwargs,
    ):
        super().__init__(master, *args, **kwargs)

        self.__db = TasksDatabase("database.db")

        self.task_id = task_id
        self.task_text = task_text
        self.about_task = about_task
        self.on_remove_task = on_remove_task
        self.show_task_frame = show_task_frame_instance

        # column configure
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)

        self.check_box = CTkCheckBox(self, text="check")
        self.check_box.grid(row=0, column=0)

        self.task_btn = CTkButton(
            self, text=self.task_text, command=self.open_about_task
        )
        self.task_btn.grid(row=0, column=1)

        self.delete_button = CTkButton(self, text="remove", command=self.remove_task)
        self.delete_button.grid(row=0, column=2, sticky="nsew", padx=10, pady=5)

        self.all_about_task_root = None

    def remove_task(self):
        if self.on_remove_task:
            self.on_remove_task(self.task_id)

            self.__db.remove(self.task_id)

    def open_about_task(self):
        if (
            self.all_about_task_root is None
            or not self.all_about_task_root.winfo_exists()
        ):
            self.all_about_task_root = AllAboutTask(
                self.task_id, self.task_text, self.about_task, self.show_task_frame
            )

        else:
            self.all_about_task_root.focus_force()
            self.all_about_task_root.lift()
