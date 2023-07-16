from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

root = Tk()
root.title("Array Record")
root.geometry("1080x720")
my_tree = ttk.Treeview(root)

# DB
config = {
    'user':'root',
    'password':'root',
    'host':'127.0.0.1',
    'port':8889,
    'database':'array_rec.db',
    'raise_on_warnings':True
}

# GUI
nimLabel = Label(root, text="NIM", font=('Arial', 15))
namaLabel = Label(root, text="Nama", font=('Arial', 15))
nimLabel.grid(row=1, column=0, padx=10)
namaLabel.grid(row=2, column=0, padx=10)

nimEntry = Entry(root, font=('Arial', 15), width=20)
namaEntry = Entry(root, font=('Arial', 15), width=20)
nimEntry.grid(row=1, column=1)
namaEntry.grid(row=2, column=1)

nilaiDisipLabel = Label(root, text="Nilai Disiplin (25%)", font=('Arial', 15))
nilaiEtikaLabel = Label(root, text="Nilai Etika (25%)", font=('Arial', 15))
nilaiDisipLabel.grid(row=1, column=2)
nilaiEtikaLabel.grid(row=2, column=2)

nilaiDisipEntry = Entry(root, font=('Arial', 15), width=20)
nilaiEtikaEntry = Entry(root, font=('Arial', 15), width=20)
nilaiDisipEntry.grid(row=1, column=3)
nilaiEtikaEntry.grid(row=2, column=3)

root.mainloop()