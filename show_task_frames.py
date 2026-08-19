from customtkinter import *

from add_task import AddTask
from dashboard import DashboardTopLevel
from task_frame import TaskFrame
from tasks_database import TasksDatabase


class ShowTasksFrame(CTkFrame):
    def __init__(self, master, username, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.__db = TasksDatabase("database.db", username)

        self.username = username

        # column configure
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=12)
        self.columnconfigure(2, weight=1)

        self.search_input = CTkEntry(
            self, corner_radius=25, placeholder_text="search the task", width=580
        )
        self.search_input.grid(column=1, row=0, sticky="ns", pady=10)

        self.search_input.bind("<KeyRelease>", self.search)

        self.add_button = CTkButton(self, text="+", command=self.open_add)
        self.add_button.grid(column=2, row=0, sticky="e", pady=10, padx=(0, 10))

        self.open_dashboard_btn = CTkButton(
            self, text="open beta dashboard", command=self.open_dashboard
        )
        self.open_dashboard_btn.grid(column=0, row=0)

        self.dashboard_root = None

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
            task_frame.grid(
                column=0, columnspan=3, row=row_index, pady=5, padx=20, sticky="nsew"
            )

            self.task_widgets[task_id] = task_frame

    def refresh_tasks(self):
        self.load_tasks()

    def handle_task_removal(self, removed_task_id):
        if removed_task_id in self.task_widgets:
            widget_to_remove = self.task_widgets[removed_task_id]
            widget_to_remove.destroy()
            del self.task_widgets[removed_task_id]

        self.refresh_tasks()

    def search(self, e):
        text = self.search_input.get().lower().strip()

        row = 1

        for task in self.task_widgets.values():
            if text in task.task_text.lower():
                task.grid(
                    row=row, column=0, columnspan=3, padx=20, pady=5, sticky="nsew"
                )

                row += 1

            else:
                task.grid_forget()

    def open_dashboard(self):
        if self.dashboard_root is None or not self.dashboard_root.winfo_exists():
            self.dashboard_root = DashboardTopLevel(self, username=self.username)
        else:
            self.dashboard_root.focus()
