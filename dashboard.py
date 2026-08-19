from customtkinter import *


class DashboardTopLevel(CTkToplevel):
    def __init__(self, *args, username: str, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Dashboard")
        self.geometry("650x500")

        # write username in dashboard and user can change acount or make acount

        # column configure
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # row configure
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.title_frame = CTkFrame(self, corner_radius=25)
        self.title_frame.grid(row=0, column=1, sticky="n")

        self.title_lbl = CTkLabel(
            self.title_frame,
            text="Beta Dashboard",
        )
        self.title_lbl.grid(row=0, column=0, pady=10, padx=20)

        self.username_lbl = CTkLabel(
            self, text=f"user: {username}", font=CTkFont(weight="bold")
        )
        self.username_lbl.grid(row=0, column=0, sticky="nw", pady=10, padx=10)

        self.finished_tasks = CTkFrame(self, corner_radius=25)
        self.finished_tasks.grid(row=1, column=0, sticky="sew", padx=7, pady=(0, 10))

        self.make_lbl(self.finished_tasks, "Finished Tasks")

        self.total_task = CTkFrame(self, corner_radius=25)
        self.total_task.grid(row=1, column=1, sticky="sew", padx=7, pady=(0, 10))

        self.make_lbl(self.total_task, "Total Tasks")



        self.unfinished_tasks = CTkFrame(self, corner_radius=25)
        self.unfinished_tasks.grid(row=1, column=2, sticky="sew", padx=7, pady=(0, 10))

        self.make_lbl(self.unfinished_tasks, "Unfinished Tasks")

    def make_lbl(self, president: CTkFrame, title: str, values: int | None = None):
        title_lbl = CTkLabel(president, text=title)
        title_lbl.pack()

        if not values:
            value_lbl = CTkLabel(president, text="it's don't work cause beta")
            value_lbl.pack()
