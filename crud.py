from tkinter import ttk, messagebox
from tkinter import *
import mysql.connector

root = Tk()
root.title("CRUD APP")
root.geometry("830x400")
my_tree = ttk.Treeview(root)

config = {
    'user':'root',
    'password':'root',
    'host':'127.0.0.1',
    'port':8889,
    'database':'crud.db',
    'raise_on_warnings':True
}

# FUNCTION 
def reverse(tuples):
    newTup = tuples[::-1]
    return newTup

# FUNCTION READ DATA
def read():
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tb_data")
        result = cursor.fetchall()
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
        conn.close()
    return result

# FUNCTION GET VALUE FROM TREE
def getValue(event):
    nikEntry.delete(0, END)
    namaEntry.delete(0, END)
    alamatEntry.delete(0, END)
    row_id = my_tree.selection()[0]
    select = my_tree.set(row_id)
    nikEntry.insert(0, select['NIK'])
    namaEntry.insert(0, select['Nama'])
    alamatEntry.insert(0, select['Alamat'])

# FUNCTION INSERT QUERY
def insert(nik, nama, alamat):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tb_data VALUES ('" + str(nik) + "','" + str(nama) + "', '" + str(alamat) + "')")
        conn.commit()
        messagebox.showinfo("information", "Data Inserted Successfully.")
        nikEntry.delete(0, END)
        namaEntry.delete(0, END)
        alamatEntry.delete(0, END)
        nikEntry.focus_set()
    except Exception as e:
        print(e)
        conn.rollback()
        conn.close()

# FUNCTION INSERT
def insert_data():
    if len(nikEntry.get()) <= 5:
        messagebox.showinfo("information", "NIK is too short.")
        nikEntry.focus_set()
    elif nikEntry.get().isdigit() == False:
        messagebox.showinfo("information", "NIK must be a number.")
        nikEntry.focus_set()
    elif len(namaEntry.get()) <= 1:
        messagebox.showinfo("information", "Nama is too short.")
        namaEntry.focus_set()
    elif namaEntry.get().isdigit() == True:
        messagebox.showinfo("information", "Nama must be Alphabetical.")
        namaEntry.focus_set()
    elif len(alamatEntry.get()) <= 1:
        messagebox.showinfo("information", "Alamat is too short.")
        alamatEntry.focus_set()
    elif alamatEntry.get().isdigit() == True:
        messagebox.showinfo("information", "Alamat must be Alphabetical.")
        alamatEntry.focus_set()
    else:
        answer = messagebox.askokcancel("question", "Insert this data?")
        if answer:
            nik = str(nikEntry.get())
            nama = str(namaEntry.get())
            alamat = str(alamatEntry.get())
            insert(str(nik), str(nama), str(alamat))
        else:
            messagebox.showinfo("information", "Insert Data Cancelled.")
    
    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag='orow')

    my_tree.tag_configure('orow', font=('Arial Bold', 15))
    my_tree.place(x=12, y=180)

# FUNCTION DELETE QUERY
def delete(data):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tb_data WHERE nik = '" + str(data) + "'")
        conn.commit()
        messagebox.showinfo("information", "Data Deleted Successfully.")
        nikEntry.delete(0, END)
        namaEntry.delete(0, END)
        alamatEntry.delete(0, END)
        nikEntry.focus_set()
    except Exception as e:
        print(e)
        conn.rollback()
        conn.close()

# FUNCTION DELETE
def delete_data():
    selectedItem = my_tree.selection()[0]
    deleteData = str(my_tree.item(selectedItem)['values'][0])
    answer = messagebox.askokcancel("question", "Delete this data?")
    if answer:
        delete(deleteData)
    else:
        messagebox.showinfo("information", "Delete Data Cancelled.")

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag='orow')

    my_tree.tag_configure('orow', font=('Arial Bold', 15))
    my_tree.place(x=12, y=180)

# FUNCTION UPDATE QUERY
def update(nik, nama, alamat, idNik):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("UPDATE tb_data SET nik = '" + str(nik) + "', nama = '" + str(nama) + "', alamat = '" + str(alamat) + "' WHERE nik = '" + str(idNik) + "'")
        conn.commit()
        messagebox.showinfo("information", "Data Updated Successfully.")
        nikEntry.delete(0, END)
        namaEntry.delete(0, END)
        alamatEntry.delete(0, END)
        nikEntry.focus_set()
    except Exception as e:
        print(e)
        conn.rollback()
        conn.close()

# FUNCTION UPDATE
def update_data():
    selectedItem = my_tree.selection()[0]
    updateData = my_tree.item(selectedItem)['values'][0]

    if len(nikEntry.get()) <= 5:
        messagebox.showinfo("information", "NIK is too short.")
        nikEntry.focus_set()
    elif nikEntry.get().isdigit() == False:
        messagebox.showinfo("information", "NIK must be a number.")
        nikEntry.focus_set()
    elif len(namaEntry.get()) <= 1:
        messagebox.showinfo("information", "Nama is too short.")
        namaEntry.focus_set()
    elif namaEntry.get().isdigit() == True:
        messagebox.showinfo("information", "Nama must be Alphabetical.")
        namaEntry.focus_set()
    elif len(alamatEntry.get()) <= 1:
        messagebox.showinfo("information", "Alamat is too short.")
        alamatEntry.focus_set()
    elif alamatEntry.get().isdigit() == True:
        messagebox.showinfo("information", "Alamat must be Alphabetical.")
        alamatEntry.focus_set()
    else:
        answer = messagebox.askokcancel("question", "Update this data?")
        if answer:
            nik = str(nikEntry.get())
            nama = str(namaEntry.get())
            alamat = str(alamatEntry.get())
            update(nik, nama, alamat, updateData)
        else:
            messagebox.showinfo("information", "Update Data Cancelled.")

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag='orow')

    my_tree.tag_configure('orow', font=('Arial Bold', 15))
    my_tree.place(x=12, y=180)

# GUI
nikLabel = Label(root,text="NIK", font=('Arial', 15), anchor=W, justify=LEFT)
namaLabel = Label(root, text="Nama Lengkap", font=('Arial', 15), anchor=W, justify=LEFT)
alamatLabel = Label(root, text="Alamat", font=('Arial', 15), anchor=W, justify=LEFT)
nikLabel.grid(row=1, column=0, sticky=W, padx=10, pady=5)
namaLabel.grid(row=2, column=0,sticky=W, padx=10, pady=5)
alamatLabel.grid(row=3, column=0, sticky=W, padx=10, pady=5)

nikEntry = Entry(root, font=('Arial', 15), justify=LEFT)
namaEntry = Entry(root, font=('Arial', 15), justify=LEFT)
alamatEntry = Entry(root, font=('Arial', 15), justify=LEFT)
nikEntry.grid(row=1, column=1, sticky=W, padx=5, pady=5)
namaEntry.grid(row=2, column=1, sticky=W, padx=5, pady=5)
alamatEntry.grid(row=3, column=1, sticky=W, padx=5, pady=5)

btnSimpan = Button(root, text="Simpan", font=('Arial', 15), justify=LEFT, width=5, height=2, command=insert_data)
btnEdit = Button(root, text="Edit", font=('Arial', 15), justify=LEFT, width=5, height=2, command=update_data)
btnHapus = Button(root, text="Hapus", font=('Arial', 15), justify=LEFT, width=5, height=2, command=delete_data)
btnTutup = Button(root, text="Tutup", font=('Arial', 15), justify=LEFT, width=5, height=2, command=root.destroy)
btnSimpan.place(x=10, y=125)
btnEdit.place(x=90, y=125)
btnHapus.place(x=170, y=125)
btnTutup.place(x=250, y=125)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))
my_tree["columns"] = ("NIK", "Nama", "Alamat")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("NIK", anchor=N, width=200)
my_tree.column("Nama", anchor=N, width=200)
my_tree.column("Alamat", anchor=N, width=400)

my_tree.heading("NIK", text="NIK")
my_tree.heading("Nama", text="Nama Lengkap")
my_tree.heading("Alamat", text="Alamat")

for data in my_tree.get_children():
    my_tree.delete(data)

for result in reverse(read()):
    my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag='orow')

my_tree.tag_configure('orow', font=('Arial Bold', 15))
my_tree.place(x=12, y=180)
my_tree.bind("<Double-Button-1>", getValue)

root.mainloop()
