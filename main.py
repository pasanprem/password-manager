from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    var_website = input_website.get()
    var_email = input_email.get()
    var_password = input_password.get()
    data_row = f"{var_website} | {var_email} | {var_password}\n"

    file = open("data.txt","a")
    file.write(data_row)
    file.close()

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
button_password = Button(text="Generate Password")
button_password.grid(column=2,row=3,sticky="W")

# Add button (1,4,span=2)
button_add = Button(text="Add",width=36,command=save)
button_add.grid(column=1,row=4,columnspan=2,sticky="EW")


window.mainloop()