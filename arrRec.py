from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

root = Tk()
root.title("Array Record")
root.geometry("1420x376")
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

def reverse(tuples):
    newTup = tuples[::-1]
    return newTup

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

# FUNCTION GET VALUE
def getValue(event):
    nimEntry.delete(0, END)
    namaEntry.delete(0, END)
    nilaiDisipEntry.delete(0, END)
    nilaiEtikaEntry.delete(0, END)
    nilaiEtosEntry.delete(0, END)
    nilaiInovasiEntry.delete(0, END)
    row_id = my_tree.selection()[0]
    select = my_tree.set(row_id)
    nimEntry.insert(0, select['NIM'])
    namaEntry.insert(0, select['Nama'])
    nilaiDisipEntry.insert(0, select['Disiplin'])
    nilaiEtikaEntry.insert(0, select['Etika'])
    nilaiEtosEntry.insert(0, select['Etos'])
    nilaiInovasiEntry.insert(0, select['Inovasi'])

# FUNCTION INSERT
def insert(nim, nama, disip, etika, etos, inovasi, disip1, etika1, etos1, inovasi1, total, mutu, keterangan):
    if len(nimEntry.get()) < 5:
        messagebox.showinfo("information", "NIM is too short.")
        nimEntry.focus_set()
    elif len(namaEntry.get()) < 5:
        messagebox.showinfo("information", "Nama is too short.")
        namaEntry.focus_set()
    elif len(nilaiDisipEntry.get()) <= 1:
        messagebox.showinfo("information", "Input Nilai Disipilin from 10 to 100.")
        nilaiDisipEntry.focus_set()
    elif len(nilaiEtikaEntry.get()) <= 1:
        messagebox.showinfo("information", "Input Nilai Etika from 10 to 100.")
        nilaiEtikaEntry.focus_set()
    elif len(nilaiEtosEntry.get()) <= 1:
        messagebox.showinfo("information", "Input Nilai Etos from 10 to 100.")
        nilaiEtosEntry.focus_set()
    elif len(nilaiInovasiEntry.get()) <= 1:
        messagebox.showinfo("information", "Input Nilai Inovasi from 10 to 100.")
        nilaiInovasiEntry.focus_set()
    else:
        answer = messagebox.askokcancel("Question", "Insert this data?")
        if answer:
            try:
                conn = mysql.connector.connect(**config)
                cursor = conn.cursor()
                cursor.execute("INSERT INTO tb_data VALUES ('" + str(nim) + "','" + str(nama) + "','" + str(disip) + "','" + str(etika) + "','" + str(etos) + "','" + str(inovasi) + "','" + str(disip1) + "','" + str(etika1) + "','" + str(etos1) + "','" + str(inovasi1) + "','" + str(total) + "','" + str(mutu) + "','" + str(keterangan) + "')")
                messagebox.showinfo("information", "Data Inserted Successfully.")
                conn.commit()
                nimEntry.delete(0, END)
                namaEntry.delete(0, END)
                nilaiDisipEntry.delete(0, END)
                nilaiEtikaEntry.delete(0, END)
                nilaiEtosEntry.delete(0, END)
                nilaiInovasiEntry.delete(0, END)
                nimEntry.focus_set()
            except Exception as e:
                print(e)
                conn.rollback()
                conn.close()
        else:
            messagebox.showinfo("information", "Insert Cancelled.")
            nimEntry.delete(0, END)
            namaEntry.delete(0, END)
            nilaiDisipEntry.delete(0, END)
            nilaiEtikaEntry.delete(0, END)
            nilaiEtosEntry.delete(0, END)
            nilaiInovasiEntry.delete(0, END)
            nimEntry.focus_set()

def insert_data():
    try:
        nim = str(nimEntry.get())
        nama = str(namaEntry.get())
        disip = int(nilaiDisipEntry.get())
        etika = int(nilaiEtikaEntry.get())
        etos = int(nilaiEtosEntry.get())
        inovasi = int(nilaiInovasiEntry.get())
        
        disip1 = disip * 0.25
        etika1 = etika * 0.25
        etos1 = etos * 0.25
        inovasi1 = inovasi * 0.25
        total = disip1 + etika1 + etos1 + inovasi1
        if total >= 90:
            mutu = "A"
            keterangan = "LULUS"
        elif total >= 75 and total < 90:
            mutu = "B"
            keterangan = "LULUS"
        elif total >= 60 and total < 75:
            mutu = "C"
            keterangan = "LULUS"
        elif total >= 50 and total < 60:
            mutu = "D"
            keterangan = "TIDAK LULUS"
        else:
            mutu = "E"
            keterangan = "TIDAK LULUS"
        insert(int(nim), str(nama), float(disip), float(disip1), float(etika), float(etika1), float(etos), float(etos1), float(inovasi), float(inovasi1), float(total), str(mutu), str(keterangan))

        for data in my_tree.get_children():
            my_tree.delete(data)

        for result in reverse(read()):
            my_tree.insert(parent="", index="end", iid=result, text="", values=(result), tag="orow")

        my_tree.tag_configure('orow', font=('Arial Bold', 15))
        my_tree.place(x=12, y=150)
    except Exception as e:
        if nim == "" or nim == " ":
            messagebox.showinfo("information", "NIM can't be empty.")
            nimEntry.focus_set()
        elif nama == "" or nama == " ":
            messagebox.showinfo("information", "Nama can't be empty.")
            namaEntry.focus_set()
        else:
            print(e)

# FUNCTION DELETE
def delete(data):
    answer = messagebox.askokcancel("Question","Delete this data?")
    if answer:
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tb_data WHERE nim = '" + str(data) + "'")
            conn.commit()
            messagebox.showinfo("Information","Data Deleted Successfully")
        except Exception as e:
            print(e)
            conn.rollback()
            conn.close()
    else:
        messagebox.showinfo("information", "Delete Cancelled.")

def delete_data():
    selected_item = my_tree.selection()[0]
    deleteData = str(my_tree.item(selected_item)['values'][0])
    delete(deleteData)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent="", index="end", iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', font=('Arial Bold', 15))
    my_tree.place(x=12, y=150)

# FUNCTION UPDATE
def update(nim, nama, disip, etika, etos, inovasi, disip1, etika1, etos1, inovasi1, total, mutu, keterangan, idNim):
    answer = messagebox.askokcancel("question", "Update this data?")
    if answer:
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute("UPDATE tb_data SET nim = '" + str(nim) + "', nama = '" + str(nama) + "', nilai_disiplin = '" + str(disip) + "', total_disiplin = '" + str(disip1) + "', nilai_etika = '" + str(etika) + "', total_etika = '" + str(etika1) + "', nilai_etos = '" + str(etos) + "', total_etos = '" + str(etos1) + "', nilai_inovasi = '" + str(inovasi) + "', total_inovasi = '" + str(inovasi1) + "', total = '" + str(total) + "', mutu = '" + str(mutu) + "', keterangan = '" + str(keterangan) + "' WHERE nim = '" + str(idNim) + "'")
            conn.commit()
            messagebox.showinfo("information", "Data Updated Successfully.")
            nimEntry.delete(0, END)
            namaEntry.delete(0, END)
            nilaiDisipEntry.delete(0, END)
            nilaiEtikaEntry.delete(0, END)
            nilaiEtosEntry.delete(0, END)
            nilaiInovasiEntry.delete(0, END)
        except Exception as e:
            print(e)
            conn.rollback()
            conn.close()
    else:
        messagebox.showinfo("information","Update Cancelled.")

def update_data():
    try:
        selected_item = my_tree.selection()[0]
        updateNim = my_tree.item(selected_item)['values'][0]
        nim = str(nimEntry.get())
        nama = str(namaEntry.get())
        disip = int(nilaiDisipEntry.get())
        etika = int(nilaiEtikaEntry.get())
        etos = int(nilaiEtosEntry.get())
        inovasi = int(nilaiInovasiEntry.get())
        disip1 = disip * 0.25
        etika1 = etika * 0.25
        etos1 = etos * 0.25
        inovasi1 = inovasi * 0.25
        total = disip1 + etika1 + etos1 + inovasi1
        if total >= 90:
            mutu = "A"
            keterangan = "LULUS"
        elif total >= 75 and total < 90:
            mutu = "B"
            keterangan = "LULUS"
        elif total >= 60 and total < 75:
            mutu = "C"
            keterangan = "LULUS"
        elif total >= 50 and total < 60:
            mutu = "D"
            keterangan = "TIDAK LULUS"
        else:
            mutu = "E"
            keterangan = "TIDAK LULUS"

        update(str(nim), str(nama), int(disip), int(etika), int(etos), int(inovasi), int(disip1), int(etika1), int(etos1), int(inovasi1), str(total), str(mutu), str(keterangan), updateNim)

        for data in my_tree.get_children():
            my_tree.delete(data)

        for result in reverse(read()):
            my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag='orow')

        my_tree.tag_configure('orow', font=('Arial Bold', 15))
        my_tree.place(x=12, y=150)
    except Exception as e:
        print(e)

# GUI
nimLabel = Label(root, text="NIM", font=('Arial', 15))
namaLabel = Label(root, text="Nama", font=('Arial', 15))
nimLabel.grid(row=1, column=0, padx=10, pady=10)
namaLabel.grid(row=2, column=0, padx=10, pady=10)
nimEntry = Entry(root, font=('Arial', 15), width=15)
namaEntry = Entry(root, font=('Arial', 15), width=15)
nimEntry.grid(row=1, column=1)
namaEntry.grid(row=2, column=1)

nilaiDisipLabel = Label(root, text="Nilai Disiplin (25%)", font=('Arial', 15))
nilaiEtikaLabel = Label(root, text="Nilai Etika (25%)", font=('Arial', 15))
nilaiDisipLabel.grid(row=1, column=2, padx=10, pady=10)
nilaiEtikaLabel.grid(row=2, column=2, padx=10, pady=10)
nilaiDisipEntry = Entry(root, font=('Arial', 15), width=15)
nilaiEtikaEntry = Entry(root, font=('Arial', 15), width=15)
nilaiDisipEntry.grid(row=1, column=3)
nilaiEtikaEntry.grid(row=2, column=3)

nilaiEtosLabel = Label(root, text="Nilai Etos (25%)", font=('Arial', 15))
nilaiInovasiLabel = Label(root, text="Nilai Inovasi (25%)", font=('Arial', 15))
nilaiEtosLabel.grid(row=1, column=4, padx=10, pady=10)
nilaiInovasiLabel.grid(row=2, column=4, padx=10, pady=10)
nilaiEtosEntry = Entry(root, font=('Arial', 15), width=15)
nilaiInovasiEntry = Entry(root, font=('Arial', 15), width=15)
nilaiEtosEntry.grid(row=1, column=5)
nilaiInovasiEntry.grid(row=2, column=5)

buttonSimpan = Button(root, text="Simpan", font=('Arial', 15), width=10, height=2, command=insert_data)
buttonSimpan.grid(row=7, column=0, padx=10, pady=10)

buttonHapus = Button(root, text="Hapus", font=('Arial', 15), width=10, height=2, command=delete_data)
buttonHapus.grid(row=7, column=1, padx=10, pady=10)

buttonEdit = Button(root, text="Edit", font=('Arial', 15), width=10, height=2, command=update_data)
buttonEdit.grid(row=7, column=2, padx=10, pady=10)

buttonTutup = Button(root, text="Tutup", font=('Arial', 15), width=10, height=2, command=root.destroy)
buttonTutup.grid(row=7, column=3, padx=10, pady=10)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))

my_tree["columns"] = ("NIM", "Nama", "Disiplin", "Disiplin1", "Etika", "Etika1", "Etos", "Etos1", "Inovasi", "Inovasi1", "Total", "Mutu", "Keterangan")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("NIM", anchor=N, width=100)
my_tree.column("Nama", anchor=N, width=150)
my_tree.column("Disiplin", anchor=N, width=100)
my_tree.column("Disiplin1", anchor=N, width=120)
my_tree.column("Etika", anchor=N, width=100)
my_tree.column("Etika1", anchor=N, width=120)
my_tree.column("Etos", anchor=N, width=100)
my_tree.column("Etos1", anchor=N, width=120)
my_tree.column("Inovasi", anchor=N, width=100)
my_tree.column("Inovasi1", anchor=N, width=120)
my_tree.column("Total", anchor=N, width=70)
my_tree.column("Mutu", anchor=N, width=70)
my_tree.column("Keterangan", anchor=N, width=120)

my_tree.heading("NIM", text="NIM")
my_tree.heading("Nama", text="Nama")
my_tree.heading("Disiplin", text="Disiplin")
my_tree.heading("Disiplin1", text="Disiplin (25%)")
my_tree.heading("Etika", text="Etika Kerja")
my_tree.heading("Etika1", text="Etika (25%)")
my_tree.heading("Etos", text="Etos")
my_tree.heading("Etos1", text="Etos (25%)")
my_tree.heading("Inovasi", text="Inovasi")
my_tree.heading("Inovasi1", text="Inovasi (25%)")
my_tree.heading("Total", text="Total")
my_tree.heading("Mutu", text="Mutu")
my_tree.heading("Keterangan", text="Keterangan")

for data in my_tree.get_children():
    my_tree.delete(data)

for result in reverse(read()):
    my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag='orow')

my_tree.tag_configure('orow', font=('Arial Bold', 15))
my_tree.place(x=12, y=150)
my_tree.bind("<Double-Button-1>", getValue)

root.mainloop()