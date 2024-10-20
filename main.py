from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    if len(password.get()) > 0:
        password.delete(0, END)

    password.insert(0, "".join(password_list))
    pyperclip.copy(password.get())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website.get()) == 0 or len(password.get()) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website.get(),
                                       message=f"These are the details entered:\n Email: {username.get()}\n Password: {password.get()} \n Is ok to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website.get()} | {username.get()} | {password.get()} \n")
                website.delete(0, END)
                username.delete(0, END)
                username.insert(0, "georgianapal@gmail.com")
                password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title("My Password Manager")
window.config(padx=30, pady=30)

# Logo setup
canvas = Canvas(height=200, width=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Components set-up
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website = Entry(width=36)
website.grid(column=1, row=1, columnspan=2)
website.focus()

username = Entry(width=36)
username.grid(column=1, row=2, columnspan=2)
username.insert(0, "georgianapal@gmail.com")

password = Entry(width=21)
password.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", width=11, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
