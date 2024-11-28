import tkinter as tk
from tkinter import messagebox
import customtkinter
import os

# ambil data buku dari data.json
import json
with open("data.json", "r") as file:
    data = json.load(file)
    list_buku = data['list_buku']
    list_peminjaman = data['list_peminjaman']
    list_pengembalian = data['list_pengembalian']


# Custom Tkinter System Setting
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# Window or frame
app = customtkinter.CTk()
app.geometry("1080x720")
app.title("Sistem Pendataan Perpustakaan")

# Spacing no text
spacing = customtkinter.CTkLabel(app, text="")
spacing.pack()

def show_main_menu():
    for widget in app.winfo_children():
        widget.pack_forget()
    
    welcome_label = customtkinter.CTkLabel(app, text="Selamat Datang di Sistem Pendataan Perpustakaan",  font=("montserrat", 34, 'bold'))
    welcome_label.pack(pady=120)

    welcome_label = customtkinter.CTkLabel(app, text="Pilihan Menu :",  font=("montserrat", 22, 'bold'), justify="center")
    welcome_label.pack(pady=20)

    btn_crud_buku = customtkinter.CTkButton(app, text="Management Buku", command=show_crud_buku, font=("montserrat", 16))
    btn_crud_buku.pack(pady=10)

    btn_crud_peminjaman = customtkinter.CTkButton(app, text="Management Peminjaman", command=show_crud_peminjaman, font=("montserrat", 16))
    btn_crud_peminjaman.pack(pady=10)

    btn_crud_pengembalian = customtkinter.CTkButton(app, text="Management Pengembalian", command=show_crud_pengembalian, font=("montserrat", 16))
    btn_crud_pengembalian.pack(pady=10)

def show_crud_buku():
    for widget in app.winfo_children():
        widget.pack_forget()

    welcome_label = customtkinter.CTkLabel(app, text="Pilihan Menu CRUD Buku :",  font=("montserrat", 26, 'bold'))
    welcome_label.pack(pady=120)
    
    btn_create_buku = customtkinter.CTkButton(app, text="Tambahkan Data Buku", command=create_buku, font=("montserrat", 16))
    btn_create_buku.pack(pady=10)

    btn_read_buku = customtkinter.CTkButton(app, text="Tampilkan List Data Buku", command=read_buku, font=("montserrat", 16))
    btn_read_buku.pack(pady=10)

    btn_update_buku = customtkinter.CTkButton(app, text="Update Data Buku", font=("montserrat", 16))
    btn_update_buku.pack(pady=10)

    btn_delete_buku = customtkinter.CTkButton(app, text="Menghapus Data Buku", command=delete_buku, font=("montserrat", 16))
    btn_delete_buku.pack(pady=10)

    btn_back = customtkinter.CTkButton(app, text="Back", command=show_main_menu, width=10)
    btn_back.pack(pady=30)

def show_crud_peminjaman():
    for widget in app.winfo_children():
        widget.pack_forget()

    welcome_label = customtkinter.CTkLabel(app, text="Pilihan Menu CRUD Peminjaman :",  font=("montserrat", 26, 'bold'))
    welcome_label.pack(pady=120)
    
    btn_create_peminjaman = customtkinter.CTkButton(app, text="Tambahkan Data Peminjaman", font=("montserrat", 16))
    btn_create_peminjaman.pack(pady=10)

    btn_read_peminjaman = customtkinter.CTkButton(app, text="Tampilkan List Data Peminjaman", font=("montserrat", 16))
    btn_read_peminjaman.pack(pady=10)

    btn_update_peminjaman = customtkinter.CTkButton(app, text="Update Data Peminjaman", font=("montserrat", 16))
    btn_update_peminjaman.pack(pady=10)

    btn_delete_peminjaman = customtkinter.CTkButton(app, text="Menghapus Data Peminjaman", font=("montserrat", 16))
    btn_delete_peminjaman.pack(pady=10)

    btn_back = customtkinter.CTkButton(app, text="Back", command=show_main_menu, width=10)
    btn_back.pack(pady=30)

def show_crud_pengembalian():
    for widget in app.winfo_children():
        widget.pack_forget()

    welcome_label = customtkinter.CTkLabel(app, text="Pilihan Menu CRUD Pengembalian :",  font=("montserrat", 26, 'bold'))
    welcome_label.pack(pady=120)
    
    btn_create_pengembalian = customtkinter.CTkButton(app, text="Tambahkan Data Pengembalian", font=("montserrat", 16))
    btn_create_pengembalian.pack(pady=10)

    btn_read_pengembalian = customtkinter.CTkButton(app, text="Tampilkan List Data Pengembalian", font=("montserrat", 16))
    btn_read_pengembalian.pack(pady=10)

    btn_update_pengembalian = customtkinter.CTkButton(app, text="Update Data Pengembalian", font=("montserrat", 16))
    btn_update_pengembalian.pack(pady=10)

    btn_delete_pengembalian = customtkinter.CTkButton(app, text="Menghapus Data Pengembalian", font=("montserrat", 16))
    btn_delete_pengembalian.pack(pady=10)

    btn_back = customtkinter.CTkButton(app, text="Back", command=show_main_menu, width=10)
    btn_back.pack(pady=30)

def create_buku():
    for widget in app.winfo_children():
        widget.pack_forget()

    welcome_label = customtkinter.CTkLabel(app, text="Tambahkan Data Buku",  font=("montserrat", 32,'bold'))
    welcome_label.pack(pady=40)

    label_judul = customtkinter.CTkLabel(app, text="Judul Buku :", font=("montserrat", 16))
    label_judul.pack(pady=10)

    entry_judul = customtkinter.CTkEntry(app)
    entry_judul.pack(pady=2)

    label_pengarang = customtkinter.CTkLabel(app, text="Pengarang :", font=("montserrat", 16))
    label_pengarang.pack(pady=10)

    entry_pengarang = customtkinter.CTkEntry(app)
    entry_pengarang.pack(pady=2)

    label_penerbit = customtkinter.CTkLabel(app, text="Penerbit :", font=("montserrat", 16))    
    label_penerbit.pack(pady=10)

    entry_penerbit = customtkinter.CTkEntry(app)
    entry_penerbit.pack(pady=2)

    label_tahun_terbit = customtkinter.CTkLabel(app, text="Tahun Terbit :", font=("montserrat", 16))
    label_tahun_terbit.pack(pady=10)

    entry_tahun_terbit = customtkinter.CTkEntry(app)
    entry_tahun_terbit.pack(pady=2)

    label_stok = customtkinter.CTkLabel(app, text="Stok :", font=("montserrat", 16))
    label_stok.pack(pady=10)

    entry_stok = customtkinter.CTkEntry(app)
    entry_stok.pack(pady=2)

    label_rak = customtkinter.CTkLabel(app, text="Rak Buku :", font=("montserrat", 16))
    label_rak.pack(pady=10)

    entry_rak = customtkinter.CTkEntry(app)
    entry_rak.pack(pady=4)

    btn_submit = customtkinter.CTkButton(app, text="Submit", command=lambda: submit_buku(entry_judul.get(), entry_pengarang.get(), entry_penerbit.get(), entry_tahun_terbit.get(), entry_stok.get(), entry_rak.get()), width=10)
    btn_submit.pack(pady=10)
    
    btn_back = customtkinter.CTkButton(app, text="Back", command=show_crud_buku, width=10)
    btn_back.pack(pady=10)
    
def delete_buku():
    for widget in app.winfo_children():
        widget.pack_forget()

    welcome_label = customtkinter.CTkLabel(app, text="Hapus Data Buku",  font=("montserrat", 32,'bold'))
    welcome_label.pack(pady=120)

    label_id = customtkinter.CTkLabel(app, text="ID Buku :", font=("montserrat", 16))
    label_id.pack(pady=10)

    entry_id = customtkinter.CTkEntry(app)
    entry_id.pack(pady=4)
    
    btn_submit = customtkinter.CTkButton(app, text="Submit", command=lambda: del_buku(entry_id.get()), width=10)
    btn_submit.pack(pady=10)

    btn_back = customtkinter.CTkButton(app, text="Back", command=show_crud_buku, width=10)
    btn_back.pack(pady=10)


list_buku = []
list_peminjaman = []
list_pengembalian = []

def submit_buku(judul, pengarang, penerbit, tahun_terbit, stok, rak):
    list_buku.append({
        "id_buku": len(list_buku) + 1,
        "judul": judul,
        "pengarang": pengarang,
        "penerbit": penerbit,
        "tahun_terbit": tahun_terbit,
        "stock": stok,
        "rak": rak
    })

    with open("data.json", "w") as file:
        json.dump({
            "list_buku": list_buku,
            "list_peminjaman": list_peminjaman,
            "list_pengembalian": list_pengembalian
        }, file, indent=4)

    messagebox.showinfo("Success", "Data Buku Berhasil Ditambahkan")

    show_crud_buku()
    
def del_buku(id_buku):
    id_buku = int(id_buku)
    with open("data.json", "r") as file:
        data = json.load(file)
        list_buku = data['list_buku']
    if id_buku > len(list_buku) or id_buku < 1:
        messagebox.showerror("Error", "ID Buku Tidak Ditemukan")
    else:
        list_buku.pop(id_buku - 1)
        with open("data.json", "w") as file:
            json.dump({
                "list_buku": list_buku,
                "list_peminjaman": list_peminjaman,
                "list_pengembalian": list_pengembalian
            }, file, indent=4)
        messagebox.showinfo("Success", "Data Buku Berhasil Dihapus")

    show_crud_buku()

class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []

    def add_item(self, item, image=None):
        label = customtkinter.CTkLabel(self, text=item, image=image, compound="center", padx=5, anchor="w")
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        self.label_list.append(label)

# make a scrollable frame to display the list of books in the library using tkinter gui
def read_buku():
    for widget in app.winfo_children():
        widget.pack_forget()

    with open("data.json", "r") as file:
        data = json.load(file)
        list_buku = data['list_buku']

    welcome_label = customtkinter.CTkLabel(app, text="List Data Buku",  font=("montserrat", 24))
    welcome_label.pack(pady=20)

    frame = ScrollableLabelButtonFrame(app)
    frame.pack(expand=True, fill="both")

    for buku in list_buku:
        frame.add_item(f"ID Buku: {buku['id_buku']}, Judul: {buku['judul']}, Pengarang: {buku['pengarang']}, Penerbit: {buku['penerbit']}, Tahun Terbit: {buku['tahun_terbit']}, Stok: {buku['stock']}, Rak: {buku['rak']}")
    
    btn_back = customtkinter.CTkButton(app, text="Back", command=show_crud_buku, width=10)
    btn_back.pack(pady=15)

show_main_menu()

# run the app
app.mainloop()