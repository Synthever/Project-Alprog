import tkinter as tk
from tkinter import messagebox
import customtkinter
import os

# ambil data buku dari data.json
import json


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
    
    welcome_label = customtkinter.CTkLabel(app, text="Selamat Datang di Sistem Pendataan Perpustakaan",  font=("montserrat", 24))
    welcome_label.pack(pady=20)

    welcome_label = customtkinter.CTkLabel(app, text="Pilihan Menu Yang Tersedia :",  font=("montserrat", 24))
    welcome_label.pack(pady=20)

    btn_crud_buku = customtkinter.CTkButton(app, text="Management Buku", command=show_crud_buku)
    btn_crud_buku.pack(pady=10)

    btn_crud_peminjaman = customtkinter.CTkButton(app, text="Management Peminjaman", command=show_crud_peminjaman)
    btn_crud_peminjaman.pack(pady=10)

    btn_crud_pengembalian = customtkinter.CTkButton(app, text="Management Pengembalian", command=show_crud_pengembalian)
    btn_crud_pengembalian.pack(pady=10)

def show_crud_buku():
    for widget in app.winfo_children():
        widget.pack_forget()

    welcome_label = customtkinter.CTkLabel(app, text="Pilihan Menu CRUD Buku :",  font=("montserrat", 24))
    welcome_label.pack(pady=20)
    
    btn_create_buku = customtkinter.CTkButton(app, text="Tambahkan Data Buku", command=create_buku)
    btn_create_buku.pack(pady=10)

    btn_read_buku = customtkinter.CTkButton(app, text="Tampilkan list Data Buku", command=read_buku)
    btn_read_buku.pack(pady=10)

    btn_update_buku = customtkinter.CTkButton(app, text="Update Data Buku")
    btn_update_buku.pack(pady=10)

    btn_delete_buku = customtkinter.CTkButton(app, text="Menghapus Data Buku")
    btn_delete_buku.pack(pady=10)

    btn_back = customtkinter.CTkButton(app, text="Back", command=show_main_menu)
    btn_back.pack(pady=10)

def show_crud_peminjaman():
    for widget in app.winfo_children():
        widget.pack_forget()

    welcome_label = customtkinter.CTkLabel(app, text="Pilihan Menu CRUD Peminjaman :",  font=("montserrat", 24))
    welcome_label.pack(pady=20)
    
    btn_create_peminjaman = customtkinter.CTkButton(app, text="Tambahkan Data Peminjaman")
    btn_create_peminjaman.pack(pady=10)

    btn_read_peminjaman = customtkinter.CTkButton(app, text="Tampilkan list Data Peminjaman")
    btn_read_peminjaman.pack(pady=10)

    btn_update_peminjaman = customtkinter.CTkButton(app, text="Update Data Peminjaman")
    btn_update_peminjaman.pack(pady=10)

    btn_delete_peminjaman = customtkinter.CTkButton(app, text="Menghapus Data Peminjaman")
    btn_delete_peminjaman.pack(pady=10)

    btn_back = customtkinter.CTkButton(app, text="Back", command=show_main_menu)
    btn_back.pack(pady=10)

def show_crud_pengembalian():
    for widget in app.winfo_children():
        widget.pack_forget()

    welcome_label = customtkinter.CTkLabel(app, text="Pilihan Menu CRUD Pengembalian :",  font=("montserrat", 24))
    welcome_label.pack(pady=20)
    
    btn_create_pengembalian = customtkinter.CTkButton(app, text="Tambahkan Data Pengembalian")
    btn_create_pengembalian.pack(pady=10)

    btn_read_pengembalian = customtkinter.CTkButton(app, text="Tampilkan list Data Pengembalian")
    btn_read_pengembalian.pack(pady=10)

    btn_update_pengembalian = customtkinter.CTkButton(app, text="Update Data Pengembalian")
    btn_update_pengembalian.pack(pady=10)

    btn_delete_pengembalian = customtkinter.CTkButton(app, text="Menghapus Data Pengembalian")
    btn_delete_pengembalian.pack(pady=10)

    btn_back = customtkinter.CTkButton(app, text="Back", command=show_main_menu)
    btn_back.pack(pady=10)

def create_buku():
    for widget in app.winfo_children():
        widget.pack_forget()

    welcome_label = customtkinter.CTkLabel(app, text="Tambahkan Data Buku",  font=("montserrat", 24))
    welcome_label.pack(pady=20)

    label_judul = customtkinter.CTkLabel(app, text="Judul Buku :")
    label_judul.pack(pady=10)

    entry_judul = customtkinter.CTkEntry(app)
    entry_judul.pack(pady=2)

    label_pengarang = customtkinter.CTkLabel(app, text="Pengarang :")
    label_pengarang.pack(pady=10)

    entry_pengarang = customtkinter.CTkEntry(app)
    entry_pengarang.pack(pady=2)

    label_penerbit = customtkinter.CTkLabel(app, text="Penerbit :")
    label_penerbit.pack(pady=10)

    entry_penerbit = customtkinter.CTkEntry(app)
    entry_penerbit.pack(pady=2)

    label_tahun_terbit = customtkinter.CTkLabel(app, text="Tahun Terbit :")
    label_tahun_terbit.pack(pady=10)

    entry_tahun_terbit = customtkinter.CTkEntry(app)
    entry_tahun_terbit.pack(pady=2)

    label_stok = customtkinter.CTkLabel(app, text="Stok :")
    label_stok.pack(pady=10)

    entry_stok = customtkinter.CTkEntry(app)
    entry_stok.pack(pady=2)

    label_rak = customtkinter.CTkLabel(app, text="Rak buku :")
    label_rak.pack(pady=10)

    entry_rak = customtkinter.CTkEntry(app)
    entry_rak.pack(pady=2)

    btn_submit = customtkinter.CTkButton(app, text="Submit", command=lambda: submit_buku(entry_judul.get(), entry_pengarang.get(), entry_penerbit.get(), entry_tahun_terbit.get(), entry_stok.get(), entry_rak.get()))
    btn_submit.pack(pady=10)
    
    btn_back = customtkinter.CTkButton(app, text="Back", command=show_crud_buku)
    btn_back.pack(pady=15)

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
        frame.add_item(f"Judul: {buku['judul']}, Pengarang: {buku['pengarang']}, Penerbit: {buku['penerbit']}, Tahun Terbit: {buku['tahun_terbit']}, Stok: {buku['stock']}, Rak: {buku['rak']}")
        
    btn_back = customtkinter.CTkButton(app, text="Back", command=show_crud_buku)
    btn_back.pack(pady=15)

show_main_menu()

# run the app
app.mainloop()