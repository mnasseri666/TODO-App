from customtkinter import *

from show_task_frames import ShowTasksFrame
from tasks_database import TasksDatabase


class MainApp(CTk):
    def __init__(self, username):
        super().__init__()

        self.title("task manager")

        self.state("zoomed")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.__db = TasksDatabase("database.db")

        self.show_task_frames = ShowTasksFrame(
            self, border_color="black", border_width=3, username=username
        )
        self.show_task_frames.grid(row=0, column=0, sticky="nsew")

        self.after(100, self.state, "zoomed")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.destroy()
        self.quit()
