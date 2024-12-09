from tkinter import messagebox
import customtkinter
import keyboard
from PIL import Image

# ambil data buku dari data.json
import json
with open("data.json", "r") as file:
    data = json.load(file)
    list_buku = data['list_buku']
    list_peminjaman = data['list_peminjaman']
    list_pengembalian = data['list_pengembalian']
    auth = data['auth']


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

def auth():
    for widget in app.winfo_children():
        widget.pack_forget()

    # Create login container
    login_frame = customtkinter.CTkFrame(app)
    login_frame.pack(expand=True, padx=40, pady=40)

    # Create a container frame for login form and image
    content_frame = customtkinter.CTkFrame(login_frame)
    content_frame.pack(expand=True)
    content_frame.configure(fg_color="transparent")

    form_frame = customtkinter.CTkFrame(content_frame)
    form_frame.pack(side="left", padx=20)
    form_frame.configure(fg_color="transparent")

    # Login header
    header = customtkinter.CTkLabel(
        form_frame,
        text="Login Sistem Perpustakaan",
        font=("Montserrat", 24, "bold"),
        text_color="#1f538d"
    )
    header.pack(pady=(20, 30), padx=20)

    # Username field
    username_entry = customtkinter.CTkEntry(
        form_frame,
        placeholder_text="Username",
        width=300,
        height=40,
        font=("Montserrat", 14)
    )
    username_entry.pack(pady=10)

    # Password field 
    password_entry = customtkinter.CTkEntry(
        form_frame,
        placeholder_text="Password",
        width=300,
        height=40,
        font=("Montserrat", 14),
        show="*"
    )
    password_entry.pack(pady=10)

    def validate_login():
        with open("data.json", "r") as file:
            data = json.load(file)
            auth = data['auth']

        username = username_entry.get()
        password = password_entry.get()
        
        if username == auth["username"] and password == auth["password"]:
            show_main_menu()
        else:
            messagebox.showerror("Error", "Username atau Password salah!")

    # Login button
    def on_enter(event):
        validate_login()
    app.bind('<Return>', on_enter)
    
    login_button = customtkinter.CTkButton(
        form_frame,
        text="Login",
        command=validate_login,
        width=300,
        height=40,
        corner_radius=8,
        font=("Montserrat", 14, "bold"),
        hover_color="#1f538d"
    )
    login_button.pack(pady=20)

    # Left side - mp Image 
    image_frame = customtkinter.CTkFrame(content_frame)
    image_frame.pack(side="left", padx=20) # Changed from right to left
    image_frame.configure(fg_color="transparent")

    # Load and display mp image
    mp_image = customtkinter.CTkImage(
        light_image=Image.open("mp.png"),
        dark_image=Image.open("mp.png"),
        size=(200, 200)
    )
    mp_label = customtkinter.CTkLabel(
        image_frame,
        text="",
        image=mp_image
    )
    mp_label.pack(pady=20)

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

    # Logout button with new style
    logout_button = customtkinter.CTkButton(
        menu_frame,
        text="Logout",
        command=auth,
        font=("Montserrat", 18),
        width=300,
        height=40,
        corner_radius=10,
        hover_color="#c42b2b", 
        fg_color="#d64242"
    )
    logout_button.pack(pady=20)

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
        command=update_buku,
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

    # Create main container
    container = customtkinter.CTkFrame(app)
    container.pack(fill="both", expand=True, padx=40, pady=40)
    
    # Header
    welcome_label = customtkinter.CTkLabel(
        container, 
        text="Tambahkan Data Buku",  
        font=("Montserrat", 32, "bold"),
        text_color="#1f538d"
    )
    welcome_label.pack(pady=(20, 30))

    # Form container
    form_frame = customtkinter.CTkFrame(container)
    form_frame.pack(fill="x", padx=20)
    form_frame.grid_columnconfigure((0,1), weight=1)

    # Row 1: Judul and Pengarang
    label_judul = customtkinter.CTkLabel(form_frame, text="Judul Buku:", font=("Montserrat", 14))
    label_judul.grid(row=0, column=0, padx=10, pady=(5,0), sticky="w")
    entry_judul = customtkinter.CTkEntry(form_frame, placeholder_text="Masukkan judul buku", width=250)
    entry_judul.grid(row=1, column=0, padx=10, pady=(0,15))

    label_pengarang = customtkinter.CTkLabel(form_frame, text="Pengarang:", font=("Montserrat", 14))
    label_pengarang.grid(row=0, column=1, padx=10, pady=(5,0), sticky="w")
    entry_pengarang = customtkinter.CTkEntry(form_frame, placeholder_text="Masukkan nama pengarang", width=250)
    entry_pengarang.grid(row=1, column=1, padx=10, pady=(0,15))

    # Row 2: Penerbit and Tahun
    label_penerbit = customtkinter.CTkLabel(form_frame, text="Penerbit:", font=("Montserrat", 14))
    label_penerbit.grid(row=2, column=0, padx=10, pady=(5,0), sticky="w")
    entry_penerbit = customtkinter.CTkEntry(form_frame, placeholder_text="Masukkan nama penerbit", width=250)
    entry_penerbit.grid(row=3, column=0, padx=10, pady=(0,15))

    label_tahun_terbit = customtkinter.CTkLabel(form_frame, text="Tahun Terbit:", font=("Montserrat", 14))
    label_tahun_terbit.grid(row=2, column=1, padx=10, pady=(5,0), sticky="w")
    entry_tahun_terbit = customtkinter.CTkEntry(form_frame, placeholder_text="Masukkan tahun terbit", width=250)
    entry_tahun_terbit.grid(row=3, column=1, padx=10, pady=(0,15))

    # Row 3: Stok and Rak
    label_stok = customtkinter.CTkLabel(form_frame, text="Jumlah Stok:", font=("Montserrat", 14))
    label_stok.grid(row=4, column=0, padx=10, pady=(5,0), sticky="w")
    entry_stok = customtkinter.CTkEntry(form_frame, placeholder_text="Masukkan jumlah stok", width=250)
    entry_stok.grid(row=5, column=0, padx=10, pady=(0,15))

    label_rak = customtkinter.CTkLabel(form_frame, text="Rak Buku:", font=("Montserrat", 14))
    label_rak.grid(row=4, column=1, padx=10, pady=(5,0), sticky="w")
    entry_rak = customtkinter.CTkEntry(form_frame, placeholder_text="Masukkan nomor rak", width=250)
    entry_rak.grid(row=5, column=1, padx=10, pady=(0,15))

    # Buttons container
    button_frame = customtkinter.CTkFrame(container)
    button_frame.pack(fill="x", pady=30)
    button_frame.configure(fg_color="transparent")

    # Submit and Back buttons
    def validate_and_confirm():
        # Check if all fields are filled
        if not entry_judul.get() or not entry_pengarang.get() or not entry_penerbit.get() or \
           not entry_tahun_terbit.get() or not entry_stok.get() or not entry_rak.get():
            messagebox.showerror("Error", "Semua field harus diisi!")
            return

        # Validate numeric fields
        try:
            tahun = int(entry_tahun_terbit.get())
            stok = int(entry_stok.get())
            if tahun < 1 or stok < 0:
                messagebox.showerror("Error", "Tahun terbit dan stok harus berupa angka positif!")
                return
        except ValueError:
            messagebox.showerror("Error", "Tahun terbit dan stok harus berupa angka!")
            return
        
        # Show confirmation dialog
        if messagebox.askyesno("Konfirmasi", "Apakah anda yakin ingin menambahkan data buku ini?"):
            submit_buku(
                entry_judul.get(),
                entry_pengarang.get(),
                entry_penerbit.get(),
                tahun,
                stok,
                entry_rak.get()
            )

    # Update submit button command
    btn_submit = customtkinter.CTkButton(
        button_frame, 
        text="Submit",
        command=validate_and_confirm,
        width=200,
        height=40,
        corner_radius=8,
        font=("Montserrat", 14, "bold"),
        hover_color="#1f538d"
    )
    btn_submit.pack(side="right", padx=20)

    btn_back = customtkinter.CTkButton(
        button_frame, 
        text="← Kembali",
        command=show_crud_buku,
        width=200,
        height=40,
        corner_radius=8,
        font=("Montserrat", 14, "bold"),
        fg_color="#666666",
        hover_color="#333333"
    )
    btn_back.pack(side="left", padx=20)
    
def update_buku():
    # ubah data buku berdasarkan ID buku yang diinput user
    for widget in app.winfo_children():
        widget.pack_forget()
        
    # Create main container
    container = customtkinter.CTkFrame(app)
    container.pack(fill="both", expand=True, padx=40, pady=40)
    
    # Header
    welcome_label = customtkinter.CTkLabel(
        container, 
        text="Ubah Data Buku",  
        font=("Montserrat", 32, "bold"),
        text_color="#1f538d"
    )
    welcome_label.pack(pady=(20, 30))
    
    # Form container
    form_frame = customtkinter.CTkFrame(container)
    form_frame.pack(fill="x", padx=20)
    form_frame.grid_columnconfigure((0,1), weight=1)
    
    # ID Input
    label_id = customtkinter.CTkLabel(
        form_frame,
        text="Masukkan ID Buku yang akan diubah:",
        font=("Montserrat", 16)
    )
    label_id.grid(row=0, column=0, padx=10, pady=(0,10), sticky="w")
    
    entry_id = customtkinter.CTkEntry(
        form_frame,
        placeholder_text="ID Buku",
        width=300,
        height=40,
        font=("Montserrat", 14)
    )
    entry_id.grid(row=1, column=0, padx=10, pady=(0,20))
    
    # New data input
    label_judul = customtkinter.CTkLabel(
        form_frame,
        text="Judul Buku Baru:",
        font=("Montserrat", 16)
    )
    
    entry_judul = customtkinter.CTkEntry(
        form_frame,
        placeholder_text="Judul Buku Baru",
        width=300,
        height=40,
        font=("Montserrat", 14)
    )
    
    label_pengarang = customtkinter.CTkLabel(
        form_frame,
        text="Pengarang Baru:",
        font=("Montserrat", 16)
    )
    
    entry_pengarang = customtkinter.CTkEntry(
        form_frame,
        placeholder_text="Pengarang Baru",
        width=300,
        height=40,
        font=("Montserrat", 14)
    )
    
    label_penerbit = customtkinter.CTkLabel(
        form_frame,
        text="Penerbit Baru:",
        font=("Montserrat", 16)
    )
    
    entry_penerbit = customtkinter.CTkEntry(
        form_frame,
        placeholder_text="Penerbit Baru",
        width=300,
        height=40,
        font=("Montserrat", 14)
    )
    
    label_tahun_terbit = customtkinter.CTkLabel(
        form_frame,
        text="Tahun Terbit Baru:",
        font=("Montserrat", 16)
    )
    
    entry_tahun_terbit = customtkinter.CTkEntry(
        form_frame,
        placeholder_text="Tahun Terbit Baru",
        width=300,
        height=40,
        font=("Montserrat", 14)
    )
    
    label_stok = customtkinter.CTkLabel(
        form_frame,
        text="Stok Baru:",
        font=("Montserrat", 16)
    )
    
    entry_stok = customtkinter.CTkEntry(
        form_frame,
        placeholder_text="Stok Baru",
        width=300,
        height=40,
        font=("Montserrat", 14)
    )
    
    label_rak = customtkinter.CTkLabel(
        form_frame,
        text="Rak Buku Baru:",
        font=("Montserrat", 16)
    )
    
    entry_rak = customtkinter.CTkEntry(
        form_frame,
        placeholder_text="Rak Buku Baru",
        width=300,
        height=40,
        font=("Montserrat", 14)
    )
    
    # Buttons container
    button_frame = customtkinter.CTkFrame(container)
    button_frame.pack(fill="x", pady=20)
    button_frame.configure(fg_color="transparent")
    
    # Submit and Back buttons
    def validate_and_update():
        with open("data.json", "r") as file:
            data = json.load(file)
            list_buku = data['list_buku']
            list_peminjaman = data['list_peminjaman']
            list_pengembalian = data['list_pengembalian']
        
        if not entry_id.get():
            messagebox.showerror("Error", "ID Buku harus diisi!")
            return
        try:
            id_buku = int(entry_id.get())
            if id_buku > len(list_buku) or id_buku < 1:
                messagebox.showerror("Error", "ID Buku Tidak Ditemukan")
            else:
                if messagebox.askyesno("Konfirmasi", "Apakah anda yakin ingin mengubah data buku ini?"):
                    list_buku[id_buku - 1]["judul"] = entry_judul.get()
                    list_buku[id_buku - 1]["pengarang"] = entry_pengarang.get()
                    list_buku[id_buku - 1]["penerbit"] = entry_penerbit.get()
                    list_buku[id_buku - 1]["tahun_terbit"] = int(entry_tahun_terbit.get())
                    list_buku[id_buku - 1]["stock"] = int(entry_stok.get())
                    list_buku[id_buku - 1]["rak"] = entry_rak.get()
                    with open("data.json", "w") as file:
                        json.dump({
                            "list_buku": list_buku,
                            "list_peminjaman": list_peminjaman,
                            "list_pengembalian": list_pengembalian
                        }, file, indent=4)
                    messagebox.showinfo("Success", "Data Buku Berhasil Diubah")
        except ValueError:
            messagebox.showerror("Error", "ID Buku harus berupa angka!")
            
    # Update submit button command
    btn_submit = customtkinter.CTkButton(
        button_frame,
        text="Ubah Buku",
        command=validate_and_update,
        width=200,
        height=40,
        corner_radius=8,
        font=("Montserrat", 14, "bold"),
        fg_color="#FF9500",
        hover_color="#FFA726"
    )
    btn_submit.pack(side="right", padx=20)
    
    btn_back = customtkinter.CTkButton(
        button_frame,
        text="← Kembali",
        command=show_crud_buku,
        width=200,
        height=40,
        corner_radius=8,
        font=("Montserrat", 14, "bold"),
        fg_color="#666666",
        hover_color="#333333"
    )
    btn_back.pack(side="left", padx=20)
    
    # Hide all form fields initially
    label_judul.grid_forget()
    entry_judul.grid_forget()
    label_pengarang.grid_forget()
    entry_pengarang.grid_forget()
    label_penerbit.grid_forget()
    entry_penerbit.grid_forget()
    label_tahun_terbit.grid_forget()
    entry_tahun_terbit.grid_forget()
    label_stok.grid_forget()
    entry_stok.grid_forget()
    label_rak.grid_forget()
    entry_rak.grid_forget()
    
    # Function to show form fields based on ID input
    def show_form_fields():
        if not entry_id.get():
            messagebox.showerror("Error", "ID Buku harus diisi!")
            return
        try:
            id_buku = int(entry_id.get())
            if id_buku > len(list_buku) or id_buku < 1:
                messagebox.showerror("Error", "ID Buku Tidak Ditemukan")
            else:
                label_judul.grid(row=2, column=0, padx=10, pady=(5,0), sticky="w")
                entry_judul.grid(row=3, column=0, padx=10, pady=(0,15))
                label_pengarang.grid(row=2, column=1, padx=10, pady=(5,0), sticky="w")
                entry_pengarang.grid(row=3, column=1, padx=10, pady=(0,15))
                label_penerbit.grid(row=4, column=0, padx=10, pady=(5,0), sticky="w")
                entry_penerbit.grid(row=5, column=0, padx=10, pady=(0,15))
                label_tahun_terbit.grid(row=4, column=1, padx=10, pady=(5,0), sticky="w")
                entry_tahun_terbit.grid(row=5, column=1, padx=10, pady=(0,15))
                label_stok.grid(row=6, column=0, padx=10, pady=(5,0), sticky="w")
                entry_stok.grid(row=7, column=0, padx=10, pady=(0,15))
                label_rak.grid(row=6, column=1, padx=10, pady=(5,0), sticky="w")
                entry_rak.grid(row=7, column=1, padx=10, pady=(0,15))
                
                entry_judul.insert(0, list_buku[id_buku - 1]["judul"])
                entry_pengarang.insert(0, list_buku[id_buku - 1]["pengarang"])
                entry_penerbit.insert(0, list_buku[id_buku - 1]["penerbit"])
                entry_tahun_terbit.insert(0, list_buku[id_buku - 1]["tahun_terbit"])
                entry_stok.insert(0, list_buku[id_buku - 1]["stock"])
                entry_rak.insert(0, list_buku[id_buku - 1]["rak"])
        except ValueError:
            messagebox.showerror("Error", "ID Buku harus berupa angka!")
            
    # Update submit button command
    btn_submit.configure(command=validate_and_update)
    
    # Update ID entry command
    entry_id.bind("<Return>", lambda event: show_form_fields())
    
def delete_buku():
    for widget in app.winfo_children():
        widget.pack_forget()

    # Create main container
    container = customtkinter.CTkFrame(app)
    container.pack(fill="both", expand=True, padx=40, pady=40)
    
    # Header
    welcome_label = customtkinter.CTkLabel(
        container, 
        text="Hapus Data Buku",  
        font=("Montserrat", 32, "bold"),
        text_color="#1f538d"
    )
    welcome_label.pack(pady=(20, 30))

    # Form container 
    form_frame = customtkinter.CTkFrame(container)
    form_frame.pack(pady=20)
    form_frame.configure(fg_color="transparent")

    # ID Input
    label_id = customtkinter.CTkLabel(
        form_frame, 
        text="Masukkan ID Buku yang akan dihapus:", 
        font=("Montserrat", 16)
    )
    label_id.pack(pady=(0,10))

    entry_id = customtkinter.CTkEntry(
        form_frame,
        placeholder_text="ID Buku",
        width=300,
        height=40,
        font=("Montserrat", 14)
    )
    entry_id.pack(pady=(0,20))

    # Button container
    button_frame = customtkinter.CTkFrame(container)
    button_frame.pack(fill="x", pady=20)
    button_frame.configure(fg_color="transparent")

    # Submit button with validation
    def validate_and_delete():
        if not entry_id.get():
            messagebox.showerror("Error", "ID Buku harus diisi!")
            return
        try:
            id_buku = int(entry_id.get())
            if messagebox.askyesno("Konfirmasi", "Apakah anda yakin ingin menghapus data buku ini?"):
                del_buku(id_buku)
        except ValueError:
            messagebox.showerror("Error", "ID Buku harus berupa angka!")

    btn_submit = customtkinter.CTkButton(
        button_frame, 
        text="Hapus Buku",
        command=validate_and_delete,
        width=200,
        height=40,
        corner_radius=8,
        font=("Montserrat", 14, "bold"),
        fg_color="#FF3B30",
        hover_color="#FF6961"
    )
    btn_submit.pack(side="right", padx=20)

    btn_back = customtkinter.CTkButton(
        button_frame, 
        text="← Kembali",
        command=show_crud_buku,
        width=200,
        height=40,
        corner_radius=8,
        font=("Montserrat", 14, "bold"),
        fg_color="#666666",
        hover_color="#333333"
    )
    btn_back.pack(side="left", padx=20)

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
auth()
app.mainloop()