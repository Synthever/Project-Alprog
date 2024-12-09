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
    # Clear existing widgets
    for widget in app.winfo_children():
        widget.pack_forget()
    
    # Create main container frame
    container = customtkinter.CTkFrame(app)
    container.pack(fill="both", expand=True, padx=40, pady=40)
    
    # Header section with welcome text
    header_frame = customtkinter.CTkFrame(container)
    header_frame.pack(fill="x", pady=(20, 40))
    header_frame.configure(fg_color="transparent")
    
    welcome_label = customtkinter.CTkLabel(
        header_frame, 
        text="Sistem Pendataan Perpustakaan",
        font=("Montserrat", 38, "bold"),
        text_color="#1f538d"
    )
    welcome_label.pack(pady=10)
    
    subtitle = customtkinter.CTkLabel(
        header_frame,
        text="Selamat Datang di Sistem Manajemen Perpustakaan Digital",
        font=("Montserrat", 16),
        text_color="#FFFFFF"
    )
    subtitle.pack()

    # Menu buttons section
    menu_frame = customtkinter.CTkFrame(container)
    menu_frame.pack(pady=20)
    menu_frame.configure(fg_color="transparent")
    
    menu_label = customtkinter.CTkLabel(
        menu_frame,
        text="Menu Utama",
        font=("Montserrat", 24, "bold"),
        text_color="#FFFFFF"
    )
    menu_label.pack(pady=(0, 20))

    # Styled buttons with hover effects
    btn_crud_buku = customtkinter.CTkButton(
        menu_frame,
        text="Kelola Data Buku",
        command=show_crud_buku,
        font=("Montserrat", 18),
        width=300,
        height=40,
        corner_radius=10,
        hover_color="#1f538d"
    )
    btn_crud_buku.pack(pady=10)

    btn_crud_peminjaman = customtkinter.CTkButton(
        menu_frame,
        text="Kelola Peminjaman Buku",
        command=show_crud_peminjaman,
        font=("Montserrat", 18),
        width=300,
        height=40,
        corner_radius=10,
        hover_color="#1f538d"
    )
    btn_crud_peminjaman.pack(pady=10)

    btn_crud_pengembalian = customtkinter.CTkButton(
        menu_frame,
        text="Kelola Pengembalian Buku",
        command=show_crud_pengembalian,
        font=("Montserrat", 18),
        width=300,
        height=40,
        corner_radius=10,
        hover_color="#1f538d"
    )
    btn_crud_pengembalian.pack(pady=10)

def show_crud_buku():
    for widget in app.winfo_children():
        widget.pack_forget()

    # Create main container frame
    container = customtkinter.CTkFrame(app)
    container.pack(fill="both", expand=True, padx=40, pady=40)
    
    # Header section
    header_frame = customtkinter.CTkFrame(container)
    header_frame.pack(fill="x", pady=(20, 40))
    header_frame.configure(fg_color="transparent")
    
    welcome_label = customtkinter.CTkLabel(
        header_frame, 
        text="Menu Kelola Buku",
        font=("Montserrat", 38, "bold"),
        text_color="#1f538d"
    )
    welcome_label.pack(pady=10)
    
    subtitle = customtkinter.CTkLabel(
        header_frame,
        text="Silahkan pilih menu yang tersedia",
        font=("Montserrat", 16),
        text_color="#FFFFFF"
    )
    subtitle.pack()

    # Menu buttons section
    menu_frame = customtkinter.CTkFrame(container)
    menu_frame.pack(pady=20)
    menu_frame.configure(fg_color="transparent")

    # Create a grid of buttons
    btn_read_buku = customtkinter.CTkButton(
        menu_frame,
        text="List Data Buku",
        command=read_buku,
        font=("Montserrat", 18),
        width=300,
        height=60,
        corner_radius=15,
        hover_color="#1f538d",
        fg_color="#2b6595"
    )
    btn_read_buku.pack(pady=15)

    btn_create_buku = customtkinter.CTkButton(
        menu_frame,
        text="Tambah Data Buku",
        command=create_buku,
        font=("Montserrat", 18),
        width=300,
        height=60,
        corner_radius=15,
        hover_color="#1f538d",
        fg_color="#2b6595"
    )
    btn_create_buku.pack(pady=15)

    btn_update_buku = customtkinter.CTkButton(
        menu_frame,
        text="Ubah Data Buku",
        font=("Montserrat", 18),
        width=300,
        height=60,
        corner_radius=15,
        hover_color="#1f538d",
        fg_color="#2b6595"
    )
    btn_update_buku.pack(pady=15)

    btn_delete_buku = customtkinter.CTkButton(
        menu_frame,
        text="Hapus Data Buku",
        command=delete_buku,
        font=("Montserrat", 18),
        width=300,
        height=60,
        corner_radius=15,
        hover_color="#1f538d",
        fg_color="#2b6595"
    )
    btn_delete_buku.pack(pady=15)

    # Back button with new style
    btn_back = customtkinter.CTkButton(
        container,
        text="← Kembali ke Menu Utama",
        command=show_main_menu,
        font=("Montserrat", 14),
        width=200,
        height=40,
        corner_radius=10,
        hover_color="#1f538d",
        fg_color="#333333"
    )
    btn_back.pack(pady=30)

def show_crud_peminjaman():
    for widget in app.winfo_children():
        widget.pack_forget()

    # Create main container frame
    container = customtkinter.CTkFrame(app)
    container.pack(fill="both", expand=True, padx=40, pady=40)
    
    # Header section
    header_frame = customtkinter.CTkFrame(container)
    header_frame.pack(fill="x", pady=(20, 40))
    header_frame.configure(fg_color="transparent")
    
    welcome_label = customtkinter.CTkLabel(
        header_frame, 
        text="Menu Kelola Peminjaman",
        font=("Montserrat", 38, "bold"),
        text_color="#1f538d"
    )
    welcome_label.pack(pady=10)
    
    subtitle = customtkinter.CTkLabel(
        header_frame,
        text="Silahkan pilih menu yang tersedia",
        font=("Montserrat", 16),
        text_color="#FFFFFF"
    )
    subtitle.pack()

    # Menu buttons section
    menu_frame = customtkinter.CTkFrame(container)
    menu_frame.pack(pady=20)
    menu_frame.configure(fg_color="transparent")

    # Create styled buttons
    btn_read_peminjaman = customtkinter.CTkButton(
        menu_frame,
        text="List Data Peminjaman",
        font=("Montserrat", 18),
        width=300,
        height=60,
        corner_radius=15,
        hover_color="#1f538d",
        fg_color="#2b6595"
    )
    btn_read_peminjaman.pack(pady=15)

    btn_create_peminjaman = customtkinter.CTkButton(
        menu_frame,
        text="Tambah Peminjaman Baru",
        font=("Montserrat", 18),
        width=300,
        height=60,
        corner_radius=15,
        hover_color="#1f538d",
        fg_color="#2b6595"
    )
    btn_create_peminjaman.pack(pady=15)

    btn_update_peminjaman = customtkinter.CTkButton(
        menu_frame,
        text="Ubah Data Peminjaman",
        font=("Montserrat", 18),
        width=300,
        height=60,
        corner_radius=15,
        hover_color="#1f538d",
        fg_color="#2b6595"
    )
    btn_update_peminjaman.pack(pady=15)

    btn_delete_peminjaman = customtkinter.CTkButton(
        menu_frame,
        text="Hapus Data Peminjaman",
        font=("Montserrat", 18),
        width=300,
        height=60,
        corner_radius=15,
        hover_color="#1f538d",
        fg_color="#2b6595"
    )
    btn_delete_peminjaman.pack(pady=15)

    # Back button with new style
    btn_back = customtkinter.CTkButton(
        container,
        text="← Kembali ke Menu Utama",
        command=show_main_menu,
        font=("Montserrat", 14),
        width=200,
        height=40,
        corner_radius=10,
        hover_color="#1f538d",
        fg_color="#333333"
    )
    btn_back.pack(pady=30)

def show_crud_pengembalian():
    for widget in app.winfo_children():
        widget.pack_forget()

    # Create main container frame
    container = customtkinter.CTkFrame(app)
    container.pack(fill="both", expand=True, padx=40, pady=40)
    
    # Header section
    header_frame = customtkinter.CTkFrame(container)
    header_frame.pack(fill="x", pady=(20, 40))
    header_frame.configure(fg_color="transparent")
    
    welcome_label = customtkinter.CTkLabel(
        header_frame, 
        text="Menu Kelola Pengembalian",
        font=("Montserrat", 38, "bold"),
        text_color="#1f538d"
    )
    welcome_label.pack(pady=10)
    
    subtitle = customtkinter.CTkLabel(
        header_frame,
        text="Silahkan pilih menu yang tersedia",
        font=("Montserrat", 16),
        text_color="#FFFFFF"
    )
    subtitle.pack()

    # Menu buttons section
    menu_frame = customtkinter.CTkFrame(container)
    menu_frame.pack(pady=20)
    menu_frame.configure(fg_color="transparent")

    # Create styled buttons
    btn_read_pengembalian = customtkinter.CTkButton(
        menu_frame,
        text="List Data Pengembalian",
        font=("Montserrat", 18),
        width=300,
        height=60,
        corner_radius=15,
        hover_color="#1f538d",
        fg_color="#2b6595"
    )
    btn_read_pengembalian.pack(pady=15)

    btn_create_pengembalian = customtkinter.CTkButton(
        menu_frame,
        text="Tambah Pengembalian Baru",
        font=("Montserrat", 18),
        width=300,
        height=60,
        corner_radius=15,
        hover_color="#1f538d",
        fg_color="#2b6595"
    )
    btn_create_pengembalian.pack(pady=15)

    btn_update_pengembalian = customtkinter.CTkButton(
        menu_frame,
        text="Ubah Data Pengembalian",
        font=("Montserrat", 18),
        width=300,
        height=60,
        corner_radius=15,
        hover_color="#1f538d",
        fg_color="#2b6595"
    )
    btn_update_pengembalian.pack(pady=15)

    btn_delete_pengembalian = customtkinter.CTkButton(
        menu_frame,
        text="Hapus Data Pengembalian",
        font=("Montserrat", 18),
        width=300,
        height=60,
        corner_radius=15,
        hover_color="#1f538d",
        fg_color="#2b6595"
    )
    btn_delete_pengembalian.pack(pady=15)

    # Back button with new style
    btn_back = customtkinter.CTkButton(
        container,
        text="← Kembali ke Menu Utama",
        command=show_main_menu,
        font=("Montserrat", 14),
        width=200,
        height=40,
        corner_radius=10,
        hover_color="#1f538d",
        fg_color="#333333"
    )
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
    
# =================================== DELETE BOOK MENU ===================================
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
# =================================== DELETE BOOK MENU ===================================

# =================================== SUBMIT BOOK FUNCTION ===================================
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
# =================================== SUBMIT BOOK FUNCTION ===================================

# =================================== DELETE BOOK FUNCTION ===================================
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
#  =================================== DELETE BOOK FUNCTION ===================================

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

# run the app
show_main_menu()
app.mainloop()