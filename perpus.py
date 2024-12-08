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
customtkinter.set_appearance_mode("dark")
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
    welcome_label.pack(pady=150)

    welcome_label = customtkinter.CTkLabel(app, text="Pilihan Menu :",  font=("montserrat", 22, 'bold'), justify="center")
    welcome_label.pack(pady=20)

    btn_crud_buku = customtkinter.CTkButton(app, text="Kelola Data Buku", command=show_crud_buku, font=("montserrat", 18), width=210, height=28)
    btn_crud_buku.pack(pady=10)

    btn_crud_peminjaman = customtkinter.CTkButton(app, text="Kelola Peminjaman Buku", command=show_crud_peminjaman, font=("montserrat", 16), width=210, height=28)
    btn_crud_peminjaman.pack(pady=10)

    btn_crud_pengembalian = customtkinter.CTkButton(app, text="Kelola Pengembalian Buku", command=show_crud_pengembalian, font=("montserrat", 16), width=210, height=28)
    btn_crud_pengembalian.pack(pady=10)

def show_crud_buku():
    for widget in app.winfo_children():
        widget.pack_forget()

    welcome_label = customtkinter.CTkLabel(app, text="Pilihan Menu Kelola Data Buku :",  font=("montserrat", 30, 'bold'))
    welcome_label.pack(pady=150)
    
    btn_read_buku = customtkinter.CTkButton(app, text="List Data Buku", command=read_buku, font=("montserrat", 16), width=210, height=28)
    btn_read_buku.pack(pady=10)

    btn_create_buku = customtkinter.CTkButton(app, text="Tambahkan Buku Baru", command=create_buku, font=("montserrat", 16), width=210, height=28)
    btn_create_buku.pack(pady=10)

    btn_update_buku = customtkinter.CTkButton(app, text="Ubah Data Buku", font=("montserrat", 16), width=210, height=28)
    btn_update_buku.pack(pady=10)

    btn_delete_buku = customtkinter.CTkButton(app, text="Hapus Data Buku", command=delete_buku, font=("montserrat", 16), width=210, height=28)
    btn_delete_buku.pack(pady=10)

    btn_back = customtkinter.CTkButton(app, text="Back", command=show_main_menu, width=10)
    btn_back.pack(pady=30)

def show_crud_peminjaman():
    for widget in app.winfo_children():
        widget.pack_forget()

    welcome_label = customtkinter.CTkLabel(app, text="Pilihan Menu Kelola Peminjaman Buku :",  font=("montserrat", 30, 'bold'))
    welcome_label.pack(pady=150)

    btn_read_peminjaman = customtkinter.CTkButton(app, text="List Data Peminjaman", font=("montserrat", 16), width=250, height=28)
    btn_read_peminjaman.pack(pady=10)

    btn_create_peminjaman = customtkinter.CTkButton(app, text="Tambah Peminjaman Baru", command=create_pinjam, font=("montserrat", 16), width=250, height=28)
    btn_create_peminjaman.pack(pady=10)

    btn_update_peminjaman = customtkinter.CTkButton(app, text="Ubah Data Peminjaman", font=("montserrat", 16), width=250, height=28)
    btn_update_peminjaman.pack(pady=10)

    btn_delete_peminjaman = customtkinter.CTkButton(app, text="Hapus Data Peminjaman", font=("montserrat", 16), width=250, height=28)
    btn_delete_peminjaman.pack(pady=10)

    btn_back = customtkinter.CTkButton(app, text="Back", command=show_main_menu, width=10)
    btn_back.pack(pady=30)

def show_crud_pengembalian():
    for widget in app.winfo_children():
        widget.pack_forget()

    welcome_label = customtkinter.CTkLabel(app, text="Pilihan Menu Kelola Pengembalian Buku :",  font=("montserrat", 30, 'bold'))
    welcome_label.pack(pady=150)
    
    btn_read_pengembalian = customtkinter.CTkButton(app, text="List Data Pengembalian", font=("montserrat", 16), width=250, height=28)
    btn_read_pengembalian.pack(pady=10)

    btn_create_pengembalian = customtkinter.CTkButton(app, text="Tambah Pengembalian Baru", font=("montserrat", 16), width=250, height=28)
    btn_create_pengembalian.pack(pady=10)

    btn_update_pengembalian = customtkinter.CTkButton(app, text="Ubah Data Pengembalian", font=("montserrat", 16), width=250, height=28)
    btn_update_pengembalian.pack(pady=10)

    btn_delete_pengembalian = customtkinter.CTkButton(app, text="Hapus Data Pengembalian", font=("montserrat", 16), width=250, height=28)
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

    label_stok = customtkinter.CTkLabel(app, text=" Jumlah Stok :", font=("montserrat", 16))
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
    welcome_label.pack(pady=150)

    label_id = customtkinter.CTkLabel(app, text="ID Buku :", font=("montserrat", 16))
    label_id.pack(pady=10)

    entry_id = customtkinter.CTkEntry(app)
    entry_id.pack(pady=4)
    
    btn_submit = customtkinter.CTkButton(app, text="Submit", command=lambda: del_buku(entry_id.get()), width=10)
    btn_submit.pack(pady=10)

    btn_back = customtkinter.CTkButton(app, text="Back", command=show_crud_buku, width=10)
    btn_back.pack(pady=10)

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

    # Create main container frame
    container = customtkinter.CTkFrame(app)
    container.pack(fill="both", expand=True, padx=20, pady=20)

    # Stylish header
    header_frame = customtkinter.CTkFrame(container)
    header_frame.pack(fill="x", pady=(0, 20))
    
    welcome_label = customtkinter.CTkLabel(
        header_frame, 
        text="List Data Buku",  
        font=("montserrat", 32, "bold"),
        text_color="#1f538d"
    )
    welcome_label.pack(pady=20)

    # Create scrollable frame with custom styling
    frame = ScrollableLabelButtonFrame(
        container,
        width=900,
        height=400,
        corner_radius=10,
        fg_color=("#FFFFFF", "#333333"),
        border_color="#1f538d",
        border_width=2
    )
    frame.pack(expand=True, fill="both", padx=20, pady=10)

    # Load and display book data with better formatting
    with open("data.json", "r") as file:
        data = json.load(file)
        list_buku = data['list_buku']

    for buku in list_buku:
        book_info = f"\tID: {buku['id_buku']} \t| Judul: {buku['judul']} | Pengarang: {buku['pengarang']} | Penerbit: {buku['penerbit']} | Tahun: {buku['tahun_terbit']} | Stok: {buku['stock']} | Rak: {buku['rak']}"
        frame.add_item(book_info)

    # Styled back button
    btn_back = customtkinter.CTkButton(
        container,
        text="← Kembali",
        command=show_crud_buku,
        width=120,
        height=32,
        corner_radius=8,
        font=("montserrat", 14, "bold"),
        hover_color="#1f538d"
    )
    btn_back.pack(pady=20)

def create_pinjam():
    for widget in app.winfo_children():
        widget.pack_forget()

    # Create main container with padding
    container = customtkinter.CTkFrame(app)
    container.pack(fill="both", expand=True, padx=30, pady=30)

    welcome_label = customtkinter.CTkLabel(
        container, 
        text="📝 Tambah Data Peminjaman",  
        font=("montserrat", 32, "bold"),
        text_color="#1f538d"
    )
    welcome_label.pack(pady=20)

    # Create form fields with better spacing and styling
    form_frame = customtkinter.CTkFrame(container)
    form_frame.pack(pady=20)

    label_id_peminjaman = customtkinter.CTkLabel(
        form_frame, 
        text="ID Peminjaman:", 
        font=("montserrat", 16, "bold")
    )
    label_id_peminjaman.pack(pady=(10, 5))

    entry_id_peminjaman = customtkinter.CTkEntry(
        form_frame,
        width=300,
        height=35,
        corner_radius=8,
        placeholder_text="Masukkan ID Peminjaman"
    )
    entry_id_peminjaman.pack()

    label_id_anggota = customtkinter.CTkLabel(
        form_frame, 
        text="ID Anggota:", 
        font=("montserrat", 16, "bold")
    )
    label_id_anggota.pack(pady=(15, 5))

    entry_id_anggota = customtkinter.CTkEntry(app)
    entry_id_anggota.pack(pady=2)

    label_id_buku = customtkinter.CTkLabel(app, text="ID Buku :", font=("montserrat", 16))    
    label_id_buku.pack(pady=10)

    entry_id_buku = customtkinter.CTkEntry(app)
    entry_id_buku.pack(pady=2)

    label_tgl_pinjam = customtkinter.CTkLabel(app, text="Tanggal Pinjam :", font=("montserrat", 16))
    label_tgl_pinjam.pack(pady=10)

    entry_tgl_pinjam = customtkinter.CTkEntry(app)
    entry_tgl_pinjam.pack(pady=2)

    label_tgl_kembali = customtkinter.CTkLabel(app, text="Tanggal Kembali :", font=("montserrat", 16))
    label_tgl_kembali.pack(pady=10)

    entry_tgl_kembali = customtkinter.CTkEntry(app)
    entry_tgl_kembali.pack(pady=2)

    label_status = customtkinter.CTkLabel(app, text="Status :", font=("montserrat", 16))
    label_status.pack(pady=10)

    entry_status = customtkinter.CTkEntry(app)
    entry_status.pack(pady=4)

    btn_submit = customtkinter.CTkButton(app, text="Submit", command=lambda: submit_pinjam(entry_id_anggota.get(), entry_id_buku.get(), entry_tgl_pinjam.get(), entry_tgl_kembali.get(), entry_status.get()), width=10)
    btn_submit.pack(pady=10)
    
    btn_back = customtkinter.CTkButton(app, text="Back", command=show_crud_peminjaman, width=10)
    btn_back.pack(pady=10)

show_main_menu()

def submit_pinjam(id_peminjaman, id_anggota, id_buku, tgl_pinjam, tgl_kembali, status):
    list_peminjaman.append({
        "id_peminjaman": len(list_peminjaman) + 1,
        "id_anggota": id_anggota,
        "id_buku": id_buku,
        "tgl_pinjam": tgl_pinjam,
        "tgl_kembali": tgl_kembali,
        "status": status
    })

    with open("data.json", "w") as file:
        json.dump({
            "list_buku": list_buku,
            "list_peminjaman": list_peminjaman,
            "list_pengembalian": list_pengembalian
        }, file, indent=4)

    messagebox.showinfo("Success", "Data Peminjaman Berhasil Ditambahkan")

    show_crud_peminjaman()

# make a scrollable frame to display the list of peminjaman in the library using tkinter gui
def read_peminjaman():
    for widget in app.winfo_children():
        widget.pack_forget()

    with open("data.json", "r") as file:
        data = json.load(file)
        list_peminjaman = data['list_peminjaman']

    welcome_label = customtkinter.CTkLabel(app, text="List Data Peminjaman",  font=("montserrat", 24))
    welcome_label.pack(pady=20)

    frame = ScrollableLabelButtonFrame(app)
    frame.pack(expand=True, fill="both")

    for peminjaman in list_peminjaman:
        frame.add_item(f"ID Peminjaman: {peminjaman['id_peminjaman']}, ID Anggota: {peminjaman['id_anggota']}, ID Buku: {peminjaman['id_buku']}, Tanggal Pinjam: {peminjaman['tgl_pinjam']}, Tanggal Kembali: {peminjaman['tgl_kembali']}, Status: {peminjaman['status']}")
    
    btn_back = customtkinter.CTkButton(app, text="Back", command=show_crud_peminjaman, width=10)
    btn_back.pack(pady=15)
    

# run the app
app.mainloop()