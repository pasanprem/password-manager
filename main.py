from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)
    #
    # password_letters = [random.choice(letters) for _ in range(nr_letters)]
    # password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    # password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]



    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password = "".join(password_list)

    input_password.delete(0, 'end')
    input_password.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    # Save inputs to variables and create one string
    var_website = input_website.get()
    var_email = input_email.get()
    var_password = input_password.get()

    if (var_website=="" or var_password==""):
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    else:
        data_row = f"{var_website} | {var_email} | {var_password}\n"

        is_ok = messagebox.askokcancel(title=input_website,message=f"These are the details entered: \nEmail: {var_email}\nPassword: {var_password}\n Is it ok to save? ")

        if is_ok:
            # Write string to the file
            with open("data.txt","a") as file:
                file.write(data_row)

            # Clear the existing fields
            input_website.delete(0,'end')
            input_email.delete(0, 'end')
            input_email.insert(0,"pasan@example.com")
            input_password.delete(0,'end')



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200,highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

## LABELS___________________________________
# Website label (0,1)
label_website = Label(text="Website: ")
label_website.grid(column=0,row=1)

# Email/Username label (0,2)
label_username = Label(text="Email/Website: ")
label_username.grid(column=0,row=2)

# Password label (0,3)
label_password = Label(text="Password: ")
label_password.grid(column=0,row=3)

## INPUTS________________________________
# Website input (1,1,span=2)
input_website = Entry(width=35)
input_website.grid(column=1,row=1,columnspan=2,sticky="EW")
input_website.focus()

# Email.. input (1,2,span=2)
input_email = Entry(width=35)
input_email.grid(column=1,row=2,columnspan=2,sticky="EW")
input_email.insert(0,"pasan@example.com")

# Password input (1,3)
input_password = Entry(width=21)
input_password.grid(column=1,row=3,sticky="EW")

## BUTTONS____________________________________
# Generate Password button (2,3)
button_password = Button(text="Generate Password",command=generate_password)
button_password.grid(column=2,row=3,sticky="W")

# Add button (1,4,span=2)
button_add = Button(text="Add",width=36,command=save)
button_add.grid(column=1,row=4,columnspan=2,sticky="EW")


window.mainloop()