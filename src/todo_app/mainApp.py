from customtkinter import *

from todo_app.show_task_frames import ShowTasksFrame


class MainApp(CTkToplevel):
    def __init__(self, login_root, username):
        super().__init__(login_root)

        self.login_root = login_root

        self.title("task manager")

        self.state("zoomed")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.show_task_frames = ShowTasksFrame(
            self,
            border_color="black",
            border_width=3,
            username=username,
        )
        self.show_task_frames.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

        self.after(100, self.state, "zoomed")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.destroy()
        self.login_root.deiconify()
