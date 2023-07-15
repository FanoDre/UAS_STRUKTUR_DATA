from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

root = Tk()
root.title("Array")
root.geometry("400x400")
my_tree = ttk.Treeview(root)

config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'port': 8889,
    'database': 'array.db',
    'raise_on_warnings': True
}

#FUNCTION
def reverse(tuples):
    newTup = tuples[::-1]
    return newTup

def GetValue(event):
    kdPosEntry.delete(0, END)
    nmDaerahEntry.delete(0, END)
    row_id = my_tree.selection()[0]
    select = my_tree.set(row_id)
    kdPosEntry.insert(0, select['Kode Pos'])
    nmDaerahEntry.insert(0, select['Nama Daerah'])

#FUNCTION READ
def read():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tb_daerah")
    result = cursor.fetchall()
    conn.commit()
    return result

#FUNCTION INSERT DATA
def insert(kdPos, nmDaerah):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tb_daerah VALUES ('" + str(kdPos) + "','" + str(nmDaerah) + "')")
    conn.commit()
    kdPosEntry.delete(0, END)
    nmDaerahEntry.delete(0, END)
    kdPosEntry.focus_set()

def insert_data():
    kdPos = str(kdPosEntry.get())
    nmDaerah = str(nmDaerahEntry.get())

    if kdPos == "" or kdPos == " ":
        messagebox.showinfo("Information","Kode Pos cant be empty.")
    elif nmDaerah == "" or nmDaerah == " ":
        messagebox.showinfo("Information","Nama Daerah cant be empty.")
    else:
        insert(str(kdPos), str(nmDaerah))
        messagebox.showinfo("information", "Data Inserted Successfully")

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow')
    my_tree.grid(row=6, column=0,columnspan=4, rowspan=5, padx=10, pady=10)

#FUNCTION HAPUS DATA
def deletee(data):
    answer = messagebox.askokcancel("Question","Delete this data?")
    if answer:
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tb_daerah WHERE kd_pos = '" + str(data) + "'")
            conn.commit()
            messagebox.showinfo("Information","Data Deleted Successfully")
            kdPosEntry.delete(0, END)
            nmDaerahEntry.delete(0, END)
            kdPosEntry.focus_set()
        except Exception as e:
            print(e)
            conn.rollback()
            conn.close()

def delete_data():
    selected_item = my_tree.selection()[0]
    deleteData = str(my_tree.item(selected_item)['values'][0])
    deletee(deleteData)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")
    
    my_tree.tag_configure('orow')
    my_tree.grid(row=6, column=0,columnspan=4, rowspan=5, padx=10, pady=10)

#FUNCTION UPDATE DATA
def update(kdPos, nmDaerah, idPos):
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
    update_name = my_tree.item(selected_item)['values'][0]
    update(kdPosEntry.get(), nmDaerahEntry.get(), update_name)
    
    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")
    
    my_tree.tag_configure('orow')
    my_tree.grid(row=6, column=0,columnspan=4, rowspan=5, padx=10, pady=10)


#GUI

kdPosLabel = Label(root, text="Kode Pos", font=('Arial Bold', 15)).place(x=10, y=10)
nmDaerahLabel = Label(root, text="Nama Daerah", font=('Arial Bold', 15)).place(x=10, y=50)

kdPosEntry = Entry(root, width=24, font=('Arial', 15)).place(x=150, y=10)
nmDaerahEntry = Entry(root, width=24, font=('Arial', 15)).place(x=150, y=50)

buttonTambah = Button(root, text="Tambah", font=('Arial', 20), bd=2, command=insert_data).place(x=10, y=100)
buttonEdit = Button(root, text="Edit", font=('Arial', 20), bd=2, command=update_data).place(x=120, y=100)
buttonHapus = Button(root, text="Hapus", font=('Arial', 20), bd=2, command=delete_data).place(x=192, y=100)
buttonTutup = Button(root, text="Tutup", font=('Arial', 20), bd=2, command=root.destroy).place(x=290, y=100)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial', 15))

my_tree['columns'] = ("Kode Pos", "Nama Daerah")
my_tree.column("#0", width=65)

my_tree.column("Kode Pos", width=100)
my_tree.column("Nama Daerah", width=200)

my_tree.heading("Kode Pos", text="Kode Pos", anchor=W)
my_tree.heading("Nama Daerah", text="Nama Daerah", anchor=W)

for data in my_tree.get_children():
    my_tree.delete(data)

for result in reverse(read()):
    my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

my_tree.tag_configure('orow' ,font=('Arial Bold', 15))
my_tree.place(x=10, y=150)

my_tree.bind('<Double-Button-1>', GetValue)

root.mainloop()