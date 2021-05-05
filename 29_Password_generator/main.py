from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = entry_website.get()
    email = entry_user_name.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please fill all fields!")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: "
                                                                f"{email}\nPassword: {password}\nIs it okay")
        if is_okay:
            with open("data.text", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                entry_website.delete(0, END)
                entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="              Website:", justify="right")
website_label.grid(column=0, row=1)

user_name_label = Label(text="Email/Username:", justify="right")
user_name_label.grid(column=0, row=2)

password_label = Label(text="              Password:")
password_label.grid(column=0, row=3)

# Entry
entry_website = Entry(width=39)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()

entry_user_name = Entry(width=39)
entry_user_name.grid(column=1, row=2, columnspan=2)
entry_user_name.insert(0, "vasha2020@gmail.com")

entry_password = Entry(width=21)
entry_password.grid(column=1, row=3)

# Buttons
generate_password = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_password.grid(column=2, row=3)

add_password = Button(text="Add", width=33, highlightthickness=0, command=save)
add_password.grid(column=1, row=4, columnspan=2)

window.mainloop()
