from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

root = Tk()
root.title("Array")
root.geometry("400x400")
my_tree = ttk.Treeview(root)

# DB
config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'port': 8889,
    'database': 'array.db',
    'raise_on_warnings': True
}

# Function 1
def reverse(tuples):
    newTup = tuples[::-1]
    return newTup

def getValue(event):
    kdPosEntry.delete(0, END)
    nmDaerahEntry.delete(0, END)
    row_id = my_tree.selection()[0]
    select = my_tree.set(row_id)
    kdPosEntry.insert(0, select['Kode Pos'])
    nmDaerahEntry.insert(0, select['Nama Daerah'])
    
def read():
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tb_daerah")
        result = cursor.fetchall()
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
        conn.close()
    return result

# Function Tambah
def insert(kdPos, nmDaerah):
    answer = messagebox.askokcancel("Question", "Insert this data?")
    if answer:
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tb_daerah VALUES ('" + str(kdPos) + "','" + str(nmDaerah) + "')")
            conn.commit()
            kdPosEntry.delete(0, END)
            nmDaerahEntry.delete(0, END)
            kdPosEntry.focus_set()
        except Exception as e:
            print(e)
            conn.rollback()
            conn.close()

def insert_data():
    kdPos = str(kdPosEntry.get())
    nmDaerah = str(nmDaerahEntry.get())
    if kdPos == "" or kdPos == " ":
        messagebox.showinfo("information", "Kode Pos can't be empty.")
    elif nmDaerah == "" or nmDaerah == " ":
        messagebox.showinfo("information","Nama Daerah can't be empty.")
    else:
        insert(str(kdPos), str(nmDaerah))
        messagebox.showinfo("information", "Data Inserted Successfully.")

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent="", index="end", iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure("orow")
    my_tree.place(x=20, y=150)

# Function Edit
def update(kdPos, nmDaerah, idPos):
    answer = messagebox.askokcancel("Question", "Update this data?")
    if answer:
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute("UPDATE tb_daerah SET kd_pos = '" + str(kdPos) + "', nm_daerah = '" + str(nmDaerah) + "' WHERE kd_pos = '" + str(idPos) + "'")
            conn.commit()
            messagebox.showinfo("information", "Data Updated Successfully")
            kdPosEntry.delete(0, END)
            nmDaerahEntry.delete(0, END)
            kdPosEntry.focus_set()
        except Exception as e:
            print(e)
            conn.rollback()
            conn.close()

def update_data():
    selected_item = my_tree.selection()[0]
    updatePos = my_tree.item(selected_item)['values'][0]
    update(kdPosEntry.get(), nmDaerahEntry.get(), updatePos)
    
    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent="", index="end", iid=result, text="", values=(result), tag="orow")
    
    my_tree.tag_configure("orow")
    my_tree.place(x=20, y=150)


# Function Delete
def delete(data):
    answer = messagebox.askokcancel("Question","Delete this data?")
    if answer:
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tb_daerah WHERE kd_pos = '" + str(data) + "'")
            conn.commit()
            messagebox.showinfo("Information","Data Deleted Successfully")
        except Exception as e:
            print(e)
            conn.rollback()
            conn.close()

def delete_data():
    selected_item = my_tree.selection()[0]
    deleteData = str(my_tree.item(selected_item)['values'][0])
    delete(deleteData)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")
    
    my_tree.tag_configure('orow')
    my_tree.place(x=20, y=150)

# GUI 
kdPosLabel = Label(root, text="Kode Pos", font=('Arial', 15))
nmDaerahLabel = Label(root, text="Nama Daerah", font=('Arial',15))
kdPosLabel.grid(row=1, column=0, padx=10, pady=10)
nmDaerahLabel.grid(row=2, column=0, padx=10, pady=10)

kdPosEntry = Entry(root, width=25, font=('Arial Bold', 15))
nmDaerahEntry = Entry(root, width=25, font=('Arial Bold', 15))
kdPosEntry.grid(row=1, column=1, columnspan=1)
nmDaerahEntry.grid(row=2, column=1, columnspan=1)

btnTambah = Button(root, text="Tambah", font=('Arial', 15), width=5, padx=5, pady=5, command=insert_data).place(x=20, y=100)
btnEdit = Button(root, text="Edit", font=('Arial', 15), width=5, padx=5, pady=5, command=update_data).place(x=110, y=100)
btnHapus = Button(root, text="Hapus", font=('Arial', 15), width=5, padx=5, pady=5, command=delete_data).place(x=200, y=100)
btnTutup = Button(root, text="Tutup", font=('Arial', 15), width=5, padx=5, pady=5, command=root.destroy).place(x=290, y=100)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))

my_tree['columns'] = ("Kode Pos", "Nama Daerah")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Kode Pos", anchor=W, width=160)
my_tree.column("Nama Daerah", anchor=W, width=200)

my_tree.heading("Kode Pos", text="Kode Pos")
my_tree.heading("Nama Daerah", text="Nama Daerah")

for data in my_tree.get_children():
    my_tree.delete(data)

for result in reverse(read()):
    my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag='orow')

my_tree.tag_configure('orow', font=('Arial Bold', 15))
my_tree.place(x=20, y=150)
my_tree.bind('<Double-Button-1>', getValue)

root.mainloop()