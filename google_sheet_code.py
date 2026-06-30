import tkinter
import gspread
from google.oauth2.service_account import Credentials

# ---------------------------- GOOGLE SHEETS SETUP ------------------------------- #
# Define the required permissions
scopes = ["https://www.googleapis.com/auth/spreadsheets"]

# Load your credentials from the JSON file you downloaded
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

# Open the Google Sheet by its exact name
sheet = client.open("Password Manager").sheet1


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Check if fields are empty to prevent saving blank rows
    if len(website) == 0 or len(password) == 0:
        print("Please don't leave any fields empty!")
        return

    # Add a new row to the Google Sheet (Pass the data as a list)
    sheet.append_row([website, email, password])

    # Clear the entries
    website_entry.delete(0, tkinter.END)
    password_entry.delete(0, tkinter.END)
    website_entry.focus()

# ... (The rest of your UI Setup code remains exactly the same) ...


