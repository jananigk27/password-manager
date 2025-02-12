from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website)==0 or len(email)==0 or len(password)==0:
            messagebox.showinfo(title="Oops", message="Please dont leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \n"
                                                   f"Password: {password}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", fg="black")
website_label.grid(column=0, row=1)
website_input = Entry(width=35, bg="white", fg="black")
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:", fg="black")
email_label.grid(column=0, row=2)
email_input = Entry(width=35, bg="white", fg="black")
email_input.insert(0, "jananigk123@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", fg="black")
password_label.grid(column=0, row=3)
password_input = Entry(width=21, bg="white", fg="black")
password_input.grid(column=1, row=3)

gen_password_button = Button(text="Generate Password", fg="black", command=generate_password)
gen_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, fg="black", command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()