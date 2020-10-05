# Using Databases SQLite: Have a look at 16-->17-->18-->19

from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('Learn To code at Codemy.com')
root.iconbitmap('/Users/baldez/Documents/GitHub/TkInter/images/Balde4.png')
root.geometry("400x400")

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create a cursor
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode interger
)
""")

# Commit Changes
conn.commit()

# Close connection
conn.close()


root.mainloop()