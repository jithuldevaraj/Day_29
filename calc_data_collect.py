def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Check if fields are empty to prevent saving blank rows
    if len(website) == 0 or len(password) == 0:
        print("Please don't leave any fields empty!")
        return

    # Open (or create) a CSV file in append mode
    # newline="" is important so Windows doesn't add extra blank rows
    with open("passwords.csv", mode="a", newline="", encoding="utf-8") as data_file:
        writer = csv.writer(data_file)

        # Write the data as a new row in the spreadsheet
        writer.writerow([website, email, password])

    # Clear the entries
    website_entry.delete(0, tkinter.END)
    password_entry.delete(0, tkinter.END)
    website_entry.focus()