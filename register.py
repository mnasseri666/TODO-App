import secrets
import string
from tkinter.messagebox import showerror, showinfo

from customtkinter import *

from userdatabase import UserDatabase


class Register(CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("500x500")
        self.title("register")

        self.fullname_check = None

        self.username_check = None

        self.password1_check = None
        self.password2_check = None

        self.pass_all_check = None

        self.__user_db = UserDatabase("database.db")

        # column configure
        self.grid_columnconfigure(0, weight=1)

        # inputs
        self.fullname_input = CTkEntry(
            self, corner_radius=15, placeholder_text="fullname(optional)", width=150
        )
        self.fullname_input.grid(row=0, column=0, pady=(10, 5))

        self.username_input = CTkEntry(
            self,
            corner_radius=15,
            placeholder_text="username(*Required)",
            width=150,
            placeholder_text_color="red",
        )
        self.username_input.grid(row=1, column=0)
        # username binds
        self.username_input.bind(
            "<KeyRelease>", lambda event: self.user_exception(event, "keyrelease")
        )
        self.username_input.bind(
            "<FocusOut>", lambda event: self.user_exception(event, "focusout")
        )
        self.username_input.bind(
            "<FocusIn>", lambda event: self.user_exception(event, "focusin")
        )
        # username lbl setting
        self.username_lbl = CTkLabel(self, text_color="red", text="u must fill this")

        self.password1_input = CTkEntry(
            self,
            corner_radius=15,
            placeholder_text="password(*Required)",
            show="*",
            width=150,
            placeholder_text_color="red",
        )
        self.password1_input.grid(row=3, column=0)
        # password1 binds
        self.password1_input.bind("<KeyRelease>", self.password_expation)
        self.password1_input.bind(
            "<FocusOut>", lambda event: self.password_expation(event, "focusout pass1")
        )
        self.password1_input.bind(
            "<FocusIn>", lambda event: self.password_expation(event, "focusin pass1")
        )
        # pass1 lbl setting
        self.password1_lbl = CTkLabel(self, text_color="red", text="u must fill this")

        self.password2_input = CTkEntry(
            self,
            corner_radius=15,
            placeholder_text="pass again(*Required)",
            show="*",
            width=150,
            placeholder_text_color="red",
        )
        self.password2_input.grid(row=6, column=0)
        # pass2 binds
        self.password2_input.bind("<KeyRelease>", self.password_expation)
        self.password2_input.bind(
            "<FocusOut>", lambda event: self.password_expation(event, "focusout pass2")
        )
        self.password2_input.bind(
            "<FocusIn>", lambda event: self.password_expation(event, "focusin pass2")
        )

        # btn
        self.submit = CTkButton(
            self, corner_radius=15, text="register user", command=self.register_user
        )
        self.submit.grid(row=7, column=0, pady=15)

        self.get_radnom_pass_btn = CTkButton(
            self,
            text="get ur random pass",
            corner_radius=15,
            command=self.get_random_pass,
        )
        self.get_radnom_pass_btn.grid(row=8, column=0)

    def register_user(self):
        fullname = self.fullname_input.get()
        username = self.username_input.get()
        password = self.password1_input.get()

        if self.pass_all_check and self.username_check and self.password2_check:
            self.__user_db.insert_to_user_db(username, fullname, password)
            showinfo("successfully", "ur account register successfully!!!")
            self.destroy()

        else:
            showerror("error", "u didn't fill ur username or password")

    def user_exception(self, e, event_type="keyrelease"):
        self.username_lbl.grid(row=2, column=0)

        username = self.username_input.get().replace(" ", "")
        username_db = self.__user_db.get_user_by_username(username)

        if event_type == "focusout":
            self.username_lbl.grid_forget()

        elif len(username) == 0:
            self.username_lbl.configure(text="u must fill this")

        elif len(username) < 6 or len(username) > 20:
            self.username_lbl.configure(text="ur user name must between 5 & 20")

        elif username_db:
            if username_db[0] == username:
                self.username_lbl.configure(text="s.o used this username")

        else:
            self.username_lbl.grid_forget()
            self.username_check = True

    def password_expation(self, e, event_type="keyrelease"):
        self.password1_lbl.grid(row=5, column=0)

        password1 = self.password1_input.get().replace(" ", "")
        password2 = self.password2_input.get().replace(" ", "")

        if event_type == "focusout pass1" or event_type == "focusout pass2":
            self.password1_lbl.grid_forget()

        elif len(password1) > 15 or 8 > len(password1):
            self.password1_lbl.configure(text="ur password must between 8 & 15")

        elif password1.isalpha():
            self.password1_lbl.configure(text="ur password must have number")

        elif password1.isnumeric():
            self.password1_lbl.configure(text="ur password must have word")

        else:
            self.password1_lbl.grid_forget()
            self.password1_check = True

        if password1 != password2:
            self.password2_input.configure(border_color="red")
            self.password2_check = False

        elif self.password1_check and password1 == password2:
            self.password2_input.configure(border_color="gray")
            self.password2_check = True

        if self.password2_check and self.password1_check:
            self.pass_all_check = True

    def get_random_pass(self):
        length = 10

        charecters = string.ascii_letters + string.digits

        password = "".join(secrets.choice(charecters) for _ in range(length))
        if password.isalpha() or password.isnumeric():
            self.get_random_pass()

        self.password1_input.delete(0, END)
        self.password1_input.insert(0, f"{password.lower()}")

        self.password1_lbl.configure(text=f"random password: {password.lower()}")
        self.password1_lbl.grid(row=5, column=0)
