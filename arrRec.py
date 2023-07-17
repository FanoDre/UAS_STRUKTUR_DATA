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
nimLabel.grid(row=1, column=0, padx=10, pady=10)
namaLabel.grid(row=2, column=0, padx=10, pady=10)

nilaiDisipLabel = Label(root, text="Nilai Disiplin (25%)", font=('Arial', 15))
nilaiEtikaLabel = Label(root, text="Nilai Etika (25%)", font=('Arial', 15))
nilaiDisipLabel.grid(row=3, column=0, padx=10, pady=10)
nilaiEtikaLabel.grid(row=4, column=0, padx=10, pady=10)

nilaiEtosLabel = Label(root, text="Nilai Etos (25%)", font=('Arial', 15))
nilaiInovasiLabel = Label(root, text="Nilai Inovasi (25%)", font=('Arial', 15))
nilaiEtosLabel.grid(row=5, column=0, padx=10, pady=10)
nilaiInovasiLabel.grid(row=6, column=0, padx=10, pady=10)

nimEntry = Entry(root, font=('Arial', 15), width=15)
namaEntry = Entry(root, font=('Arial', 15), width=15)
nimEntry.grid(row=1, column=1)
namaEntry.grid(row=2, column=1)

nilaiDisipEntry = Entry(root, font=('Arial', 15), width=15)
nilaiEtikaEntry = Entry(root, font=('Arial', 15), width=15)
nilaiDisipEntry.grid(row=3, column=1)
nilaiEtikaEntry.grid(row=4, column=1)

nilaiEtosEntry = Entry(root, font=('Arial', 15), width=15)
nilaiInovasiEntry = Entry(root, font=('Arial', 15), width=15)
nilaiEtosEntry.grid(row=5, column=1)
nilaiInovasiEntry.grid(row=6, column=1)

buttonSimpan = Button(root, text="Simpan", font=('Arial', 15), width=10, height=2)
buttonSimpan.grid(row=7, column=0, padx=10, pady=10)

buttonHapus = Button(root, text="Hapus", font=('Arial', 15), width=10, height=2)
buttonHapus.grid(row=7, column=1, padx=10, pady=10)

buttonEdit = Button(root, text="Edit", font=('Arial', 15), width=10, height=2)
buttonEdit.grid(row=7, column=2, padx=10, pady=10)

buttonTutup = Button(root, text="Tutup", font=('Arial', 15), width=10, height=2)
buttonTutup.grid(row=7, column=3, padx=10, pady=10)

root.mainloop()