from customtkinter import *

from add_task import AddTask
from task_frame import TaskFrame
from tasks_database import TasksDatabase


class ShowTasksFrame(CTkFrame):
    def __init__(self, master, username, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.__db = TasksDatabase("database.db", username)

        self.username = username

        # column configure
        self.columnconfigure(0, weight=12)
        self.columnconfigure(1, weight=1)

        self.subject_label = CTkLabel(self, text="tasks(to remove u must double click")
        self.subject_label.grid(column=0, row=0, sticky="nsew", pady=10)

        self.add_button = CTkButton(self, text="+", command=self.open_add)
        self.add_button.grid(column=1, row=0, sticky="e", pady=10)

        self.task_widgets = {}
        self.load_tasks()

        self.add_root = None

    def open_add(self):
        if self.add_root is None or not self.add_root.winfo_exists():
            self.add_root = AddTask(self, username=self.username)
        else:
            self.add_root.focus_force()
            self.add_root.lift()

    def load_tasks(self):
        for widget in self.task_widgets.values():
            widget.destroy()
        self.task_widgets = {}

        data = self.__db.read_user_tasks()

        max_row, max_col = self.grid_size()
        for r in range(1, max_row):
            self.grid_rowconfigure(r, weight=1)

        for i, task in enumerate(data):
            row_index = i + 1
            self.rowconfigure(row_index, weight=1)

            task_id = str(task[0])
            task_text = task[2]
            about_task = task[3]

            task_frame = TaskFrame(
                self, task_id, task_text, about_task, self, self.handle_task_removal
            )
            task_frame.grid(column=0, row=row_index, pady=5, padx=10, sticky="nsew")

            self.task_widgets[task_id] = task_frame

    def refresh_tasks(self):
        self.load_tasks()

    def handle_task_removal(self, removed_task_id):
        if removed_task_id in self.task_widgets:
            widget_to_remove = self.task_widgets[removed_task_id]
            widget_to_remove.destroy()
            del self.task_widgets[removed_task_id]

        self.refresh_tasks()
