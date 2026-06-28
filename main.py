import tkinter


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.configure(padx=20, pady=20, bg="black")

canvas = tkinter.Canvas(width=200, height=200, bg="white")
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

canvas.pack()


window.mainloop()
