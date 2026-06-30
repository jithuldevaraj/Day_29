import tkinter


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(event):
    # 1. Get the data
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # 2.Open the file in append mode and write the data
    with open("./data.txt", mode="a") as data_file:
        data_file.write(f"{website}  |  {email}  |  {password}\n")

    # 3.Clear the website and password entries
    website_entry.delete(0, tkinter.END)
    password_entry.delete(0, tkinter.END)

    # 4.Put the cursor back in website entry
    website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.configure(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200, bg="white")
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

canvas.grid(row=0, column=1)

#  labels and Entries
website_label = tkinter.Label(text="Website : ")
website_label.grid(row=1, column=0, sticky="E") # Aligns label to the right (East)
website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW") # Stretches to fill space
website_entry.focus()

email_label = tkinter.Label(text="Email/Username : ")
email_label.grid(row=2, column=0, sticky="E")
email_entry = tkinter.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "studynumber0001@gmail.com")

password_label= tkinter.Label(text= "Password : ")
password_label.grid(row=3, column=0, sticky="E")
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

generate_password_button = tkinter.Button(text="Generate Password")
generate_password_button.grid(row=3, column=2, sticky="EW") # Stretches to match the layout

add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")
window.bind("<Return>", save)  # Listen for the Keyboard "ENTER" key



window.mainloop()
