from tkinter.messagebox import showerror, showinfo

from customtkinter import *
from openai import OpenAI

from tasks_database import TasksDatabase


class AllAboutTask(CTkToplevel):
    def __init__(
        self, task_id, task, about_task, show_task_frame_instance, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.geometry("500x500")

        self.__db = TasksDatabase("database.db")

        self.task_text = task
        self.about_task = about_task
        self.task_id = task_id

        self.show_task_frame = show_task_frame_instance

        # row configure
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # column configure
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.task_input = CTkEntry(self, corner_radius=20)
        self.task_input.grid(row=0, column=0, columnspan=2, pady=10)
        self.task_input.insert(0, self.task_text)
        self.task_input.bind("<KeyRelease>", self.task_exception)

        self.about_task_text_box = CTkTextbox(self)
        self.about_task_text_box.grid(row=1, column=0, columnspan=2, pady=(0, 10))

        self.about_task_text_box.insert("0.0", self.about_task)

        self.edit_btn = CTkButton(
            self, text="edit", corner_radius=20, command=self.edit
        )
        self.edit_btn.grid(row=2, column=0)

        self.advice_btn = CTkButton(self, text="advice with AI", command=self.advice)
        self.advice_btn.grid(row=2, column=1)

    def edit(self):
        task_text = self.task_input.get()
        about_task = self.about_task_text_box.get("0.0", "end-1c")

        if task_text.replace(" ", ""):
            self.__db.edit_column(self.task_id, task_text, about_task)
            self.show_task_frame.refresh_tasks()
            showinfo("edited!!!", "ur task successfully edited")
            self.destroy()

        else:
            showerror("error", "u must fill task subject")

    def task_exception(self, e):
        if self.task_input.get().replace(" ", ""):
            self.task_input.configure(border_color="black")

        else:
            self.task_input.configure(border_color="red")

    def advice(self):
        client = OpenAI(
            base_url="https://api.gapgpt.app/v1",
            api_key="REMOVED_API_KEY",
        )

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": self.about_task_text_box.get("0.0", "end")}
            ],
        )

        showinfo("gpt-4o-mini", response.choices[0].message.content)
