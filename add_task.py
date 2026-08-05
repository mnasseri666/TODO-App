from tkinter.messagebox import showerror, showinfo

from customtkinter import *

from tasks_database import TasksDatabase


class AddTask(CTkToplevel):
    def __init__(self, show_task_frame_instance, username, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("500x500")

        self.show_task_frame = show_task_frame_instance
        self.username = username

        self.__db = TasksDatabase("database.db")
        self.main_frame = CTkFrame(self)

        self.task_input = CTkEntry(
            self, corner_radius=20, placeholder_text="ur task", width=350
        )
        self.task_input.pack(pady=10)
        self.task_input.bind("<KeyRelease>", self.tasks_exception)

        self.place_holder_task = "about ur task(*optional)"

        self.all_task_input = CTkTextbox(self, corner_radius=20)
        self.all_task_input.pack(pady=(0, 10))
        self.all_task_input.bind("<FocusOut>", self.task_focus_out)
        self.all_task_input.bind("<FocusIn>", self.task_focus_in)

        self.all_task_input.insert("0.0", self.place_holder_task)

        self.add_button = CTkButton(
            self, corner_radius=20, text="add task", command=self.add
        )
        self.add_button.pack()

    def add(self):
        task = self.task_input.get()
        about_task = self.all_task_input.get("0.0", "end")

        if task.replace(" ", ""):
            self.__db.add(task, about_task, self.username)
            showinfo("ok", "ur task insert successfully!!!!")
            self.task_input.delete(0, "end")
            self.all_task_input.delete("0.0", "end")
            self.all_task_input.insert("0.0", self.place_holder_task)
            self.show_task_frame.refresh_tasks()
            self.destroy()

        else:
            showerror("error!!!!", "u must fill ur task then insert it")

    def tasks_exception(self, e):
        task = self.task_input.get()

        if not task.replace(" ", ""):
            self.task_input.configure(border_color="red")

        else:
            self.task_input.configure(border_color="gray")

    def task_focus_in(self, e):
        if self.all_task_input.get("0.0", "end-1c") == self.place_holder_task:
            self.all_task_input.delete("0.0", "end")

    def task_focus_out(self, e):
        if self.all_task_input.get("0.0", "end-1c") == "":
            if len(self.all_task_input.get("0.0", "end").strip()) == 0:
                self.all_task_input.insert("0.0", self.place_holder_task)
