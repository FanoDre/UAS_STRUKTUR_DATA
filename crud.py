from tkinter import ttk, messagebox
from tkinter import *
import mysql.connector

root = Tk()
root.title("CRUD APP")
root.geometry("530x400")
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
    answer = messagebox.askokcancel("question", "Insert this data?")
    if answer:
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
    else:
        messagebox.showinfo("information", "Insert Data Cancelled.")

# FUNCTION INSERT
def insert_data():
    nik = str(nikEntry.get())
    nama = str(namaEntry.get())
    alamat = str(alamatEntry.get())

    if nik == "" or nik == " ":
        messagebox.showinfo("information", "NIK can't be empty.")
    elif nama == "" or nama == " ":
        messagebox.showinfo("information", "Nama can't be empty.")
    elif alamat == "" or alamat == " ":
        messagebox.showinfo("information", "Alamat can't be empty.")
    else:
        insert(str(nik), str(nama), str(alamat))
    
    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag='orow')

    my_tree.tag_configure('orow', font=('Arial Bold', 15))
    my_tree.place(x=12, y=180)

# FUNCTION DELETE QUERY
def delete(data):
    answer = messagebox.askokcancel("question", "Delete this data?")
    if answer:
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
    else:
        messagebox.showinfo("information", "Delete Data Cancelled.")

# FUNCTION DELETE
def delete_data():
    selectedItem = my_tree.selection()[0]
    deleteData = str(my_tree.item(selectedItem)['values'][0])
    delete(deleteData)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag='orow')

    my_tree.tag_configure('orow', font=('Arial Bold', 15))
    my_tree.place(x=12, y=180)

# FUNCTION UPDATE QUERY
def update(nik, nama, alamat, idNik):
    answer = messagebox.askokcancel("question", "Update this data?")
    if answer:
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
    else:
        messagebox.showinfo("information", "Update Data Cancelled.")

# FUNCTION UPDATE
def update_data():
    selectedItem = my_tree.selection()[0]
    updateData = my_tree.item(selectedItem)['values'][0]
    nik = str(nikEntry.get())
    nama = str(namaEntry.get())
    alamat = str(alamatEntry.get())
    if nik == "" or nik == " ":
        messagebox.showinfo("information", "NIK can't be empty.")
    elif nama == "" or nama == " ":
        messagebox.showinfo("information", "Nama can't be empty.")
    elif alamat == "" or alamat == " ":
        messagebox.showinfo("information", "Alamat can't be empty.")
    else:
        update(nik, nama, alamat, updateData)

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
my_tree.column("NIK", anchor=W, width=150)
my_tree.column("Nama", anchor=W, width=150)
my_tree.column("Alamat", anchor=W, width=200)

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
