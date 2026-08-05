from tkinter.messagebox import showerror, showinfo

from customtkinter import *

from mainApp import MainApp
from register import Register
from tasks_database import TasksDatabase
from userdatabase import UserDatabase


class Login(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("500x600")
        self.title("login")

        self.__user_db = UserDatabase("database.db")

        # column configure
        self.grid_columnconfigure(0, weight=1)

        # input
        self.username_input = CTkEntry(
            self, corner_radius=15, placeholder_text="username"
        )
        self.username_input.grid(column=0, row=0, pady=5)

        self.user_pass_input = CTkEntry(
            self, corner_radius=15, placeholder_text="password", show="*"
        )
        self.user_pass_input.grid(column=0, row=1, pady=5)

        # btn
        self.login_btn = CTkButton(
            self, corner_radius=10, text="log-in", command=self.log_in
        )
        self.login_btn.grid(column=0, row=2, pady=10)

        self.register_btn = CTkButton(
            self, corner_radius=10, text="Or Register", command=self.open_register
        )
        self.register_btn.grid(column=0, row=3)

        self.register_root = None

    def open_register(self):
        if self.register_root is None or not self.register_root.winfo_exists():
            self.register_root = Register(self)
        else:
            self.register_root.focus()

    def log_in(self):
        username = self.username_input.get()
        password = self.user_pass_input.get()

        number_not_found = 0
        number_of_users = 0

        db_values = self.__user_db.get_all_db()
        for user in db_values:
            number_of_users += 1
            if username == user[0] and password == user[2]:
                showinfo("logged in", "u log in successfully!!!")
                self.withdraw()

                self.__task_db = TasksDatabase("database.db", username)

                main_app_root = MainApp(username)
                main_app_root.mainloop()

                self.destroy()
                break

            else:
                number_not_found += 1

        if number_of_users == number_not_found:
            showerror("error", "ur username or pass is wrong")


if __name__ == "__main__":
    root = Login()
    root.mainloop()
