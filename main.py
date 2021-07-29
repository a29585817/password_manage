import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def produce_password():
    password_list1 = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list2 = [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list3 = [random.choice(numbers) for char in range(random.randint(2, 4))]
    password_list = password_list1 + password_list2 + password_list3
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    password_data = password_entry.get()
    web_data = web_entry.get()
    user_data = user_entry.get()
    new_data = {
        web_data: {
            "email": user_data,
            "password": password_data
        }
    }
    if len(web_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Empty", message="Hey don't leave column empyty!", )
    else:
        try:
            with open("store.json", mode="r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except json.decoder.JSONDecodeError:
            with open("store.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        except FileNotFoundError:
            with open("store.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("store.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


def read():
    web_data = web_entry.get().title()
    try:
        with open("store.json", mode="r") as data_file:
            data = json.load(data_file)
            get_data = data[web_data]

    except FileNotFoundError:
        tkinter.messagebox.showinfo(title="opps", message="File not found")
    except KeyError:
        print("NO key")
        tkinter.messagebox.showinfo(title="opps", message="Not this name")
    else:
        email = get_data["email"]
        password = get_data["password"]
        tkinter.messagebox.showinfo(title=web_data, message=f"Email : {email} \nPassword :{password}")
    finally:
        web_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas
canvas = tkinter.Canvas(width=200, height=200)
logo_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Label
web_label = tkinter.Label(text="Website:", )
web_label.grid(column=0, row=1)
user_label = tkinter.Label(text="Email/Username:", )
user_label.grid(column=0, row=2)
password_label = tkinter.Label(text="Password:", )
password_label.grid(column=0, row=3)

# button
start_button = tkinter.Button(text="Generate Password", command=produce_password)
start_button.grid(column=2, row=3)
add_button = tkinter.Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)
search_button = tkinter.Button(text="Search", width=15, command=read)
search_button.grid(column=2, row=1)

# Entry
web_entry = tkinter.Entry(width=21)
web_entry.grid(column=1, row=1, )
web_entry.focus()
web_data = web_entry.get()
user_entry = tkinter.Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "a0919149590@gmail.com")
password_entry = tkinter.Entry(width=21)
password_entry.grid(column=1, row=3, )

window.mainloop()
