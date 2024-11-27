import tkinter as tk
from tkinter import messagebox
import customtkinter


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

    btn_crud_buku = customtkinter.CTkButton(app, text="CRUD Buku", command=show_crud_buku)
    btn_crud_buku.pack(pady=10)

    btn_crud_peminjaman = customtkinter.CTkButton(app, text="CRUD Peminjaman", command=show_crud_peminjaman)
    btn_crud_peminjaman.pack(pady=10)

    btn_crud_pengembalian = customtkinter.CTkButton(app, text="CRUD Pengembalian", command=show_crud_pengembalian)
    btn_crud_pengembalian.pack(pady=10)

def show_crud_buku():
    for widget in app.winfo_children():
        widget.pack_forget()
    
    btn_create_buku = customtkinter.CTkButton(app, text="Create / Tambahkan Data Buku")
    btn_create_buku.pack(pady=10)

    btn_read_buku = customtkinter.CTkButton(app, text="Read / Tampilkan list Data Buku")
    btn_read_buku.pack(pady=10)

    btn_update_buku = customtkinter.CTkButton(app, text="Update / Update Data Buku")
    btn_update_buku.pack(pady=10)

    btn_delete_buku = customtkinter.CTkButton(app, text="Delete / Menghapus Data Buku")
    btn_delete_buku.pack(pady=10)

    btn_back = customtkinter.CTkButton(app, text="Back", command=show_main_menu)
    btn_back.pack(pady=10)

def show_crud_peminjaman():
    for widget in app.winfo_children():
        widget.pack_forget()
    
    btn_create_peminjaman = customtkinter.CTkButton(app, text="Create / Tambahkan Data Peminjaman")
    btn_create_peminjaman.pack(pady=10)

    btn_read_peminjaman = customtkinter.CTkButton(app, text="Read / Tampilkan list Data Peminjaman")
    btn_read_peminjaman.pack(pady=10)

    btn_update_peminjaman = customtkinter.CTkButton(app, text="Update / Update Data Peminjaman")
    btn_update_peminjaman.pack(pady=10)

    btn_delete_peminjaman = customtkinter.CTkButton(app, text="Delete / Menghapus Data Peminjaman")
    btn_delete_peminjaman.pack(pady=10)

    btn_back = customtkinter.CTkButton(app, text="Back", command=show_main_menu)
    btn_back.pack(pady=10)

def show_crud_pengembalian():
    for widget in app.winfo_children():
        widget.pack_forget()
    
    btn_create_pengembalian = customtkinter.CTkButton(app, text="Create / Tambahkan Data Pengembalian")
    btn_create_pengembalian.pack(pady=10)

    btn_read_pengembalian = customtkinter.CTkButton(app, text="Read / Tampilkan list Data Pengembalian")
    btn_read_pengembalian.pack(pady=10)

    btn_update_pengembalian = customtkinter.CTkButton(app, text="Update / Update Data Pengembalian")
    btn_update_pengembalian.pack(pady=10)

    btn_delete_pengembalian = customtkinter.CTkButton(app, text="Delete / Menghapus Data Pengembalian")
    btn_delete_pengembalian.pack(pady=10)

    btn_back = customtkinter.CTkButton(app, text="Back", command=show_main_menu)
    btn_back.pack(pady=10)

show_main_menu()


# run the app
app.mainloop()