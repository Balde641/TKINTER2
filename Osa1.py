# Kouluprojekti osa1

from tkinter import *
import sqlite3

root = Tk()
root.title('Tietokanta')
root.geometry("500x500")

# Create a database or connect to one
conn = sqlite3.connect('tasklist.db')

# Create a cursor
c = conn.cursor()

# Create table
'''
c.execute("""CREATE TABLE tasks (
    task text
)
""") 
'''
# Create Edit function to Update a record
def update():
    # Create a database or connect to one
    conn = sqlite3.connect('tasklist.db')
    # Create a cursor
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("""UPDATE tasks SET
        task = :task

        WHERE oid = :oid""", 
        {'task': task_label_editor.get(),

        'oid': record_id

        })
    
    # Commit Changes
    conn.commit()
    # Close connection
    conn.close()

    editor.destroy()


def edit():
    global editor
    editor = Tk()
    editor.title('Päivitä')
    editor.geometry("400x300")

    # Create a database or connect to one
    conn = sqlite3.connect('tasklist.db')
    # Create a cursor
    c = conn.cursor()

    record_id = delete_box.get()
    # Query the Database
    c.execute("SELECT * FROM tasks WHERE oid = " + record_id)
    records = c.fetchall()
   
    
    # Create Global Variables for text box names
    global task_label_editor
   
    # Create text Boxes
    task_label_editor = Entry(editor, width=30)
    task_label_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
  
    # Create text Box Labels
    task_label_label = Label(editor, text="Tehtävän Nimi")
    task_label_label.grid(row=0, column=0, pady=(10, 0))

     # Loop through results
    for record in records:
        task_label_editor.insert(0, record[0])
        
    # Create a Save Button To Save Edited Record
    edit_btn = Button(editor, text="Talenna Tietue", command=update, fg="green")
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=140)


# Create Function to Delete A Record
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('tasklist.db')
    # Create a cursor
    c = conn.cursor()

    # Delete a Record
    c.execute("DELETE from tasks WHERE oid = " + delete_box.get())

    delete_box.delete(0, END)

    # Commit Changes
    conn.commit()
    # Close connection
    conn.close()


# Create Fuction For Database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('tasklist.db')
    # Create a cursor
    c = conn.cursor()

    # Insert Into Table
    c.execute("INSERT INTO tasks VALUES (:task_label)",
            {
                'task_label': task_label.get()
            })

    # Commit Changes
    conn.commit()
    # Close connection
    conn.close()

    # Clear The Text Boxes
    task_label.delete(0, END)
    
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('tasklist.db')
    # Create a cursor
    c = conn.cursor()

    # Query the Database
    c.execute("SELECT *, oid FROM tasks")
    records = c.fetchall()

    # Loop through Results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + "\t" + str(record[1]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)    

    # Commit Changes
    conn.commit()
    # Close connection
    conn.close()    

# Create text Boxes
task_label = Entry(root, width=30, borderwidth=3)
task_label.grid(row=0, column=1, padx=20, pady=(10, 0))

delete_box = Entry(root, width=30, borderwidth=3)
delete_box.grid(row=9, column=1, pady=5)

# Create text Box Labels
task_label_label = Label(root, text="Tehtävän Nimi")
task_label_label.grid(row=0, column=0, pady=(10, 0))

# Create Submit Button
submit_btn = Button(root, text="Lisää Tietue Tietokantaan", command=submit, fg="green")
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Näytä Tietueet", command=query, fg="brown")
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a Delete Button
delete_btn = Button(root, text="Poista Tietueet", command=delete, fg="red")
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# Create an Update Button
edit_btn = Button(root, text="Muokkaa Tietueita", command=edit, fg="blue")
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=130)

# Commit Changes
conn.commit()

# Close connection
conn.close()


# Ohjelmaan kirjautuminen---------------------------------DOWN CHECK

# rivi 0 -------------------------------------------
l = Label(root, text = "Käyttäjätunnus:")
l.grid(row = 13, column = 0)
e = Entry(root, width = 30, bg="orange", fg="black", borderwidth=5)
e.grid(row = 13, column = 1)
e.insert(0, "Nimi: ")
# rivi 1 -------------------------------------------
l2 = Label(root, text = "Salasana:")
l2.grid(row = 14, column = 0)
e2 = Entry(root, width = 30, show = '*', bg="orange", fg="black", borderwidth=5)
e2.grid(row = 14, column = 1)
e2.insert(0, "Salasana: ")
# rivi 2 -------------------------------------------
b = Button(root, text = "KIRJAUDU SISÄÄN", fg="green")
b.grid(row = 15, column = 1)

# pitää ikkunan näkyvissä kunnes tuhoamme sen
root.mainloop() 