from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

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
input_website.grid(column=1,row=1,columnspan=2)

# Email.. input (1,2,span=2)
input_email = Entry(width=35)
input_email.grid(column=1,row=2,columnspan=2)

# Password input (1,3)
input_password = Entry(width=21)
input_password.grid(column=1,row=3)

## BUTTONS____________________________________
# Generate Password button (2,3)
button_password = Button(text="Generate Password")
button_password.grid(column=2,row=3)

# Add button (1,4,span=2)
button_add = Button(text="Add",width=36)
button_add.grid(column=1,row=4,columnspan=2)


window.mainloop()