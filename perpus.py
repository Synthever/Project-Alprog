from tkinter import messagebox
import customtkinter
from PIL import Image

# ambil data buku dari data.json
import json
with open("data.json") as file:
    data = json.load(file)
    auth = data['auth']
    list_buku = data['list_buku']
    list_peminjaman = data['list_peminjaman']
    list_pengembalian = data['list_pengembalian']
    list_anggota = data['list_anggota']


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

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! AUTH FUNCTIONS AREA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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
    image_frame.pack(side="left", padx=20) 
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
    
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! AUTH FUNCTIONS AREA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# ================================= MENU PERPUSTAKAAN =====================================

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
    
    btn_crud_anggota = customtkinter.CTkButton(
        menu_frame,
        text="Kelola Data Anggota",
        command=show_crud_anggota,
        font=("Montserrat", 18),
        width=300,
        height=40,
        corner_radius=10,
        hover_color="#1f538d"
    )
    btn_crud_anggota.pack(pady=10)

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
    
# ================================= MENU PERPUSTAKAAN =================================

# ================================= MENU PENGEMBALIAN =================================

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
    
# ================================= MENU PENGEMBALIAN =================================

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! BUKU FUNCTIONS AREA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# ====================================== MENU BUKU ======================================

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
    
# ====================================== MENU BUKU ======================================

# ================================= READ BUKU FUNCTIONS =================================

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

    # Create scrollable container
    frame = ScrollableLabelButtonFrame(
        container,
        width=900,
        height=400,
        corner_radius=10,
        fg_color=("#FFFFFF", "#333333"),
        border_color="#1f538d",
        border_width=2,
        orientation="horizontal"  # Enable horizontal scrolling
    )
    frame.pack(expand=True, fill="both", padx=20, pady=10)

    # Create inner frame for content
    inner_frame = customtkinter.CTkFrame(frame)
    inner_frame.pack(expand=True, fill="both")
    inner_frame.configure(fg_color="transparent")

    # Column headers
    headers = ["ID", "Judul", "Pengarang", "Penerbit", "Tahun", "Stok", "Rak"]
    for i, header in enumerate(headers):
        label = customtkinter.CTkLabel(
            inner_frame, 
            text=header,
            font=("Montserrat", 14, "bold"),
            width=150
        )
        label.grid(row=0, column=i, padx=5, pady=5, sticky="w")

    # Load and display data
    with open("data.json", "r") as file:
        data = json.load(file)
        list_buku = data['list_buku']

    for i, buku in enumerate(list_buku, 1):
        # ID
        customtkinter.CTkLabel(inner_frame, text=str(buku['id_buku']), width=50).grid(row=i, column=0, padx=55, pady=2, sticky="w")
        # Judul
        customtkinter.CTkLabel(inner_frame, text=buku['judul'], width=200).grid(row=i, column=1, padx=5, pady=2, sticky="w")
        # Pengarang
        customtkinter.CTkLabel(inner_frame, text=buku['pengarang'], width=150).grid(row=i, column=2, padx=5, pady=2, sticky="w")
        # Penerbit
        customtkinter.CTkLabel(inner_frame, text=buku['penerbit'], width=150).grid(row=i, column=3, padx=5, pady=2, sticky="w")
        # Tahun
        customtkinter.CTkLabel(inner_frame, text=str(buku['tahun_terbit']), width=100).grid(row=i, column=4, padx=35, pady=2, sticky="w")
        # Stok
        customtkinter.CTkLabel(inner_frame, text=str(buku['stock']), width=100).grid(row=i, column=5, padx=35, pady=2, sticky="w")
        # Rak
        customtkinter.CTkLabel(inner_frame, text=buku['rak'], width=100).grid(row=i, column=6, padx=35, pady=2, sticky="w")

    # Back button
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

# ================================= READ BUKU FUNCTIONS =================================

# ================================= CREATE BUKU FUNCTIONS ===============================

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
    button_frame.pack(fill="both", pady=30)
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
        text="← Kembali ke Menu Utama",
        command=show_crud_buku,
        width=200,
        height=40,
        corner_radius=8,
        font=("Montserrat", 14),
        hover_color="#1f538d",
        fg_color="#333333"
    )
    btn_back.pack(side="right", padx=20)
    
def submit_buku(judul, pengarang, penerbit, tahun_terbit, stok, rak):
    # Read current data
    with open("data.json", "r") as file:
        data = json.load(file)
        list_buku = data['list_buku']
        list_peminjaman = data.get('list_peminjaman', [])
        list_pengembalian = data.get('list_pengembalian', [])
        list_anggota = data.get('list_anggota', [])
        auth = data.get('auth', {})

    # Add new book
    list_buku.append({
        "id_buku": len(list_buku) + 1,
        "judul": judul,
        "pengarang": pengarang,
        "penerbit": penerbit,
        "tahun_terbit": tahun_terbit,
        "stock": stok,
        "rak": rak
    })

    # Save all data back
    with open("data.json", "w") as file:
        json.dump({
            "auth": auth,
            "list_buku": list_buku,
            "list_peminjaman": list_peminjaman, 
            "list_pengembalian": list_pengembalian,
            "list_anggota": list_anggota
        }, file, indent=4)

    messagebox.showinfo("Success", "Data Buku Berhasil Ditambahkan")
    show_crud_buku()
    
# ================================= CREATE BUKU FUNCTIONS =================================
    
# ================================= UPDATE BUKU FUNCTIONS =================================

def update_buku():
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
    
    btn_submit = customtkinter.CTkButton(
        form_frame,
        text="Submit",
        command=lambda: form_update_buku(entry_id.get()),
        width=200,
        height=40,
        corner_radius=8,
        font=("Montserrat", 14, "bold"),
        hover_color="#FFA726",
        fg_color="#FF9500"
    )
    btn_submit.grid(row=1, column=1, padx=10, pady=(0,20), sticky="ew")  # Changed to stretch horizontally
    
    # Back button
    btn_back = customtkinter.CTkButton(
        container,
        text="← Kembali ke Menu Utama",
        command=show_crud_buku,
        font=("Montserrat", 14),
        width=200,
        height=40,
        corner_radius=10,
        hover_color="#1f538d",
        fg_color="#333333"
    )
    btn_back.pack(pady=30)
    
def form_update_buku(id_buku):
    try:
        id_buku = int(id_buku)
        with open("data.json", "r") as file:
            data = json.load(file)
            list_buku = data["list_buku"]
            
        if id_buku < 1 or id_buku > len(list_buku):
            messagebox.showerror("Error", "ID Buku tidak ditemukan!")
            return
            
        buku = list_buku[id_buku-1]
        
        for widget in app.winfo_children():
            widget.pack_forget()
            
        # Create main container
        container = customtkinter.CTkFrame(app)
        container.pack(fill="both", expand=True, padx=40, pady=40)
        
        # Header
        header_label = customtkinter.CTkLabel(
            container,
            text=f"Update Buku ID: {id_buku}",
            font=("Montserrat", 32, "bold"),
            text_color="#1f538d"
        )
        header_label.pack(pady=(20, 30))

        # Form container
        form_frame = customtkinter.CTkFrame(container)
        form_frame.pack(fill="x", padx=20)
        form_frame.grid_columnconfigure((0,1), weight=1)

        # Form fields
        label_judul = customtkinter.CTkLabel(form_frame, text="Judul Buku:", font=("Montserrat", 14))
        label_judul.grid(row=0, column=0, padx=10, pady=(5,0), sticky="w")
        entry_judul = customtkinter.CTkEntry(form_frame, width=250)
        entry_judul.insert(0, buku["judul"])
        entry_judul.grid(row=1, column=0, padx=10, pady=(0,15))

        label_pengarang = customtkinter.CTkLabel(form_frame, text="Pengarang:", font=("Montserrat", 14))
        label_pengarang.grid(row=0, column=1, padx=10, pady=(5,0), sticky="w")
        entry_pengarang = customtkinter.CTkEntry(form_frame, width=250)
        entry_pengarang.insert(0, buku["pengarang"])
        entry_pengarang.grid(row=1, column=1, padx=10, pady=(0,15))

        label_penerbit = customtkinter.CTkLabel(form_frame, text="Penerbit:", font=("Montserrat", 14))
        label_penerbit.grid(row=2, column=0, padx=10, pady=(5,0), sticky="w")
        entry_penerbit = customtkinter.CTkEntry(form_frame, width=250)
        entry_penerbit.insert(0, buku["penerbit"])
        entry_penerbit.grid(row=3, column=0, padx=10, pady=(0,15))

        label_tahun = customtkinter.CTkLabel(form_frame, text="Tahun Terbit:", font=("Montserrat", 14))
        label_tahun.grid(row=2, column=1, padx=10, pady=(5,0), sticky="w")
        entry_tahun = customtkinter.CTkEntry(form_frame, width=250)
        entry_tahun.insert(0, buku["tahun_terbit"])
        entry_tahun.grid(row=3, column=1, padx=10, pady=(0,15))

        label_stok = customtkinter.CTkLabel(form_frame, text="Stok:", font=("Montserrat", 14))
        label_stok.grid(row=4, column=0, padx=10, pady=(5,0), sticky="w")
        entry_stok = customtkinter.CTkEntry(form_frame, width=250)
        entry_stok.insert(0, buku["stock"])
        entry_stok.grid(row=5, column=0, padx=10, pady=(0,15))

        label_rak = customtkinter.CTkLabel(form_frame, text="Rak:", font=("Montserrat", 14))
        label_rak.grid(row=4, column=1, padx=10, pady=(5,0), sticky="w")
        entry_rak = customtkinter.CTkEntry(form_frame, width=250)
        entry_rak.insert(0, buku["rak"])
        entry_rak.grid(row=5, column=1, padx=10, pady=(0,15))

        # Button container
        button_frame = customtkinter.CTkFrame(container)
        button_frame.pack(fill="x", pady=20)
        button_frame.configure(fg_color="transparent")

        def save_changes():
            try:
                # Validate fields
                if not all([entry_judul.get(), entry_pengarang.get(), entry_penerbit.get(),
                           entry_tahun.get(), entry_stok.get(), entry_rak.get()]):
                    messagebox.showerror("Error", "Semua field harus diisi!")
                    return
                    
                tahun = int(entry_tahun.get())
                stok = int(entry_stok.get())
                if tahun < 1 or stok < 0:
                    messagebox.showerror("Error", "Tahun dan stok harus berupa angka positif!")
                    return

                if messagebox.askyesno("Konfirmasi", "Apakah anda yakin ingin mengubah data buku ini?"):
                    # Update book data
                    list_buku[id_buku-1].update({
                        "judul": entry_judul.get(),
                        "pengarang": entry_pengarang.get(),
                        "penerbit": entry_penerbit.get(),
                        "tahun_terbit": tahun,
                        "stock": stok,
                        "rak": entry_rak.get()
                    })
                    
                    # Save to file
                    with open("data.json", "w") as file:
                        json.dump(data, file, indent=4)
                    
                    messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
                    show_crud_buku()
                    
            except ValueError:
                messagebox.showerror("Error", "Tahun dan stok harus berupa angka!")

        btn_save = customtkinter.CTkButton(
            button_frame,
            text="Simpan Perubahan",
            command=save_changes,
            width=200,
            height=40,
            corner_radius=8,
            font=("Montserrat", 14, "bold"),
            fg_color="#FF9500",
            hover_color="#FFA726"
        )
        btn_save.pack(side="right", padx=20)

        btn_back = customtkinter.CTkButton(
            button_frame,
            text="← Kembali",
            command=update_buku,
            width=200,
            height=40,
            corner_radius=8,
            font=("Montserrat", 14, "bold"),
            fg_color="#666666",
            hover_color="#333333"
        )
        btn_back.pack(side="left", padx=20)
        
    except ValueError:
        messagebox.showerror("Error", "ID Buku harus berupa angka!")
        
# ================================= UPDATE BUKU FUNCTIONS =================================

# ================================= DELETE BUKU FUNCTIONS =================================

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
    form_frame.pack(fill="x", padx=20)
    form_frame.grid_columnconfigure((0,1), weight=1)
    
    # ID Input
    label_id = customtkinter.CTkLabel(
        form_frame,
        text="Masukkan ID Buku yang akan dihapus:",
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
    
    btn_submit = customtkinter.CTkButton(
        form_frame,
        text="Submit",
        command=lambda: del_buku(entry_id.get()),
        width=200,
        height=40,
        corner_radius=8,
        font=("Montserrat", 14, "bold"),
        hover_color="#c42b2b",
        fg_color="#d64242"
    )
    btn_submit.grid(row=1, column=1, padx=10, pady=(0,20), sticky="ew")  # Changed to stretch horizontally
    
    # Back button
    btn_back = customtkinter.CTkButton(
        container,
        text="← Kembali ke Menu Utama",
        command=show_crud_buku,
        font=("Montserrat", 14),
        width=200,
        height=40,
        corner_radius=10,
        hover_color="#1f538d",
        fg_color="#333333"
    )
    btn_back.pack(pady=30)

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
    
# ================================= DELETE BUKU FUNCTIONS =================================

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! BUKU FUNCTIONS AREA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! PEMINJAMAN FUNCTIONS AREA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# ================================= MENU PEMINJAMAN =================================

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
        command=create_peminjaman,
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
    
# ================================= MENU PEMINJAMAN =======================================

# ================================= READ PEMINJAMAN FUNCTIONS =============================

def read_peminjaman():
    print("Read Peminjaman")

# ================================= READ PEMINJAMAN FUNCTIONS =============================

# ================================= CREATE PEMINJAMAN FUNCTIONS ===========================

def create_peminjaman():
    # Get current logged in user
    with open("data.json", "r") as file:
        data = json.load(file)
        current_user = data['auth']['username']
        id_petugas = data['auth']['id_user']
    
    for widget in app.winfo_children():
        widget.pack_forget()

    # Create main scrollable container that fills the entire window
    main_frame = customtkinter.CTkFrame(app)
    main_frame.pack(fill="both", expand=True, padx=0, pady=0)
    
    # Create canvas and scrollbar with full width
    canvas = customtkinter.CTkCanvas(main_frame, bg='#2b2b2b', highlightthickness=0)
    scrollbar = customtkinter.CTkScrollbar(main_frame, orientation="vertical", command=canvas.yview)
    scrollable_frame = customtkinter.CTkFrame(canvas, fg_color=("#DBDBDB", "#2b2b2b"))

    # Configure canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Bind mouse wheel
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
    # Update scroll region when frame changes
    def configure_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    scrollable_frame.bind("<Configure>", configure_scroll_region)
    
    # Create window that fills canvas width
    canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", width=canvas.winfo_width())
    
    # Update canvas window width when canvas is resized
    def configure_window_width(event):
        canvas.itemconfig(canvas_window, width=event.width)
    canvas.bind("<Configure>", configure_window_width)

    # Create container inside scrollable frame with proper padding
    container = customtkinter.CTkFrame(scrollable_frame)
    container.pack(fill="both", expand=True, padx=40, pady=40)

    # Pack canvas and scrollbar to fill window
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Header
    welcome_label = customtkinter.CTkLabel(
        container, 
        text="Tambah Data Peminjaman",  
        font=("Montserrat", 32, "bold"),
        text_color="#1f538d"
    )
    welcome_label.pack(pady=(20, 30))

    # Form container
    form_frame = customtkinter.CTkFrame(container)
    form_frame.pack(fill="x", padx=20)
    form_frame.grid_columnconfigure((0,1), weight=1)

    # Tanggal Peminjaman
    label_tgl = customtkinter.CTkLabel(form_frame, text="Tanggal Peminjaman:", font=("Montserrat", 14))
    label_tgl.grid(row=0, column=0, padx=10, pady=(5,0), sticky="w")
    
    # Create date picker frame
    date_frame = customtkinter.CTkFrame(form_frame)
    date_frame.grid(row=1, column=0, padx=10, pady=(0,15), sticky="w")
    
    # Day dropdown
    day_var = customtkinter.StringVar()
    days = [str(i).zfill(2) for i in range(1, 32)]
    day_dropdown = customtkinter.CTkOptionMenu(date_frame, variable=day_var, values=days, width=60)
    day_dropdown.pack(side="left", padx=5)
    
    # Month dropdown
    month_var = customtkinter.StringVar()
    months = [str(i).zfill(2) for i in range(1, 13)]
    month_dropdown = customtkinter.CTkOptionMenu(date_frame, variable=month_var, values=months, width=60)
    month_dropdown.pack(side="left", padx=5)
    
    # Year dropdown
    year_var = customtkinter.StringVar()
    import datetime
    current_year = datetime.datetime.now().year
    years = [str(i) for i in range(current_year, current_year + 5)]
    year_dropdown = customtkinter.CTkOptionMenu(date_frame, variable=year_var, values=years, width=80)
    year_dropdown.pack(side="left", padx=5)

    # Set default date to today
    today = datetime.datetime.now()
    day_var.set(today.strftime("%d"))
    month_var.set(today.strftime("%m"))
    year_var.set(str(today.year))

    # Buku Search Frame
    buku_frame = customtkinter.CTkFrame(form_frame)
    buku_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=(20,15), sticky="ew")
    
    label_buku = customtkinter.CTkLabel(buku_frame, text="Cari Buku:", font=("Montserrat", 14))
    label_buku.pack(pady=(10,5))
    
    search_buku_var = customtkinter.StringVar()
    search_buku_entry = customtkinter.CTkEntry(
        buku_frame, 
        placeholder_text="Masukkan judul buku",
        width=300,
        textvariable=search_buku_var
    )
    search_buku_entry.pack(pady=5)
    
    buku_list_frame = customtkinter.CTkScrollableFrame(buku_frame, height=150)
    buku_list_frame.pack(fill="x", padx=10, pady=10)
    
    selected_buku_var = customtkinter.StringVar()
    
    def search_buku(*args):
        # Clear previous results
        for widget in buku_list_frame.winfo_children():
            widget.destroy()
            
        search_term = search_buku_var.get().lower()
        for buku in data['list_buku']:
            if search_term in buku['judul'].lower():
                btn = customtkinter.CTkRadioButton(
                    buku_list_frame,
                    text=f"{buku['judul']} (ID: {buku['id_buku']})",
                    variable=selected_buku_var,
                    value=str(buku['id_buku'])
                )
                btn.pack(pady=2, anchor="w")
    
    search_buku_var.trace('w', search_buku)
    search_buku()  # Initial population
    
    # Anggota Search Frame
    anggota_frame = customtkinter.CTkFrame(form_frame)
    anggota_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=(20,15), sticky="ew")
    
    label_anggota = customtkinter.CTkLabel(anggota_frame, text="Cari Anggota:", font=("Montserrat", 14))
    label_anggota.pack(pady=(10,5))
    
    search_anggota_var = customtkinter.StringVar()
    search_anggota_entry = customtkinter.CTkEntry(
        anggota_frame, 
        placeholder_text="Masukkan nama anggota",
        width=300,
        textvariable=search_anggota_var
    )
    search_anggota_entry.pack(pady=5)
    
    anggota_list_frame = customtkinter.CTkScrollableFrame(anggota_frame, height=150)
    anggota_list_frame.pack(fill="x", padx=10, pady=10)
    
    selected_anggota_var = customtkinter.StringVar()
    
    def search_anggota(*args):
        # Clear previous results
        for widget in anggota_list_frame.winfo_children():
            widget.destroy()
            
        search_term = search_anggota_var.get().lower()
        for anggota in data['list_anggota']:
            if search_term in anggota['nama'].lower():
                btn = customtkinter.CTkRadioButton(
                    anggota_list_frame,
                    text=f"{anggota['nama']} (ID: {anggota['id_anggota']})",
                    variable=selected_anggota_var,
                    value=str(anggota['id_anggota'])
                )
                btn.pack(pady=2, anchor="w")
    
    search_anggota_var.trace('w', search_anggota)
    search_anggota()  # Initial population

    # Buttons container
    button_frame = customtkinter.CTkFrame(container)
    button_frame.pack(fill="x", pady=30)
    button_frame.configure(fg_color="transparent")

    def validate_and_save():
        try:
            # Get selected date
            selected_date = f"{year_var.get()}-{month_var.get()}-{day_var.get()}"
            tgl_pinjam = datetime.datetime.strptime(selected_date, "%Y-%m-%d")
            
            # Calculate return date (7 days from borrow date)
            tgl_kembali = tgl_pinjam + datetime.timedelta(days=7)
            
            # Validate selections
            if not selected_buku_var.get() or not selected_anggota_var.get():
                messagebox.showerror("Error", "Pilih buku dan anggota terlebih dahulu!")
                return
                
            # Format dates for JSON
            tgl_pinjam_str = tgl_pinjam.strftime("%Y-%m-%d")
            tgl_kembali_str = tgl_kembali.strftime("%Y-%m-%d")
            
            # Prepare new peminjaman data
            new_peminjaman = {
                "id_peminjaman": len(data['list_peminjaman']) + 1,
                "tanggal_peminjaman": tgl_pinjam_str,
                "tanggal_pengembalian": tgl_kembali_str,
                "id_buku": int(selected_buku_var.get()),
                "id_anggota": int(selected_anggota_var.get()),
                "id_petugas": id_petugas
            }
            
            # Update data
            data['list_peminjaman'].append(new_peminjaman)
            
            # Save to file
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
                
            messagebox.showinfo("Sukses", "Data peminjaman berhasil ditambahkan!")
            show_crud_peminjaman()
            
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

    btn_submit = customtkinter.CTkButton(
        button_frame,
        text="Submit",
        command=validate_and_save,
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
        command=show_crud_peminjaman,
        width=200,
        height=40,
        corner_radius=8,
        font=("Montserrat", 14, "bold"),
        fg_color="#666666",
        hover_color="#333333"
    )
    btn_back.pack(side="left", padx=20)

# ================================= CREATE PEMINJAMAN FUNCTIONS ===========================

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! PEMINJAMAN FUNCTIONS AREA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ANGGOTA FUNCTIONS AREA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# ================================= MENU ANGGOTA ==========================================

def show_crud_anggota():
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
    btn_read_anggota = customtkinter.CTkButton(
        menu_frame,
        text="List Data Anggota",
        command=read_anggota,
        font=("Montserrat", 18),
        width=300,
        height=60,
        corner_radius=15,
        hover_color="#1f538d",
        fg_color="#2b6595"
    )
    btn_read_anggota.pack(pady=15)

    btn_create_anggota = customtkinter.CTkButton(
        menu_frame,
        text="Tambah Anggota Baru",
        command=create_anggota,
        font=("Montserrat", 18),
        width=300,
        height=60,
        corner_radius=15,
        hover_color="#1f538d",
        fg_color="#2b6595"
    )
    btn_create_anggota.pack(pady=15)
    
    btn_update_anggota = customtkinter.CTkButton(
        menu_frame,
        text="Ubah Data Anggota",
        command=update_anggota,
        font=("Montserrat", 18),
        width=300,
        height=60,
        corner_radius=15,
        hover_color="#1f538d",
        fg_color="#2b6595"
    )
    btn_update_anggota.pack(pady=15)
    
    btn_delete_anggota = customtkinter.CTkButton(
        menu_frame,
        text="Hapus Data Anggota",
        command=delete_anggota,
        font=("Montserrat", 18),
        width=300,
        height=60,
        corner_radius=15,
        hover_color="#1f538d",
        fg_color="#2b6595"
    )
    btn_delete_anggota.pack(pady=15)

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
    
# ================================= MENU ANGGOTA =====================================

# ================================= READ ANGGOTA FUNCTIONS ================================

def read_anggota():
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
        text="List Data Anggota",  
        font=("montserrat", 32, "bold"),
        text_color="#1f538d"
    )
    welcome_label.pack(pady=20)

    # Create scrollable container
    frame = ScrollableLabelButtonFrame(
        container,
        width=900,
        height=400,
        corner_radius=10,
        fg_color=("#FFFFFF", "#333333"),
        border_color="#1f538d",
        border_width=2,
        orientation="horizontal"  # Enable horizontal scrolling
    )
    frame.pack(expand=True, fill="both", padx=20, pady=10)

    # Create inner frame for content
    inner_frame = customtkinter.CTkFrame(frame)
    inner_frame.pack(expand=True, fill="both")
    inner_frame.configure(fg_color="transparent")

    # Column headers
    headers = ["ID", "Username", "Nama", "Gender", "Telp", "Alamat", "Email"]
    for i, header in enumerate(headers):
        label = customtkinter.CTkLabel(
            inner_frame, 
            text=header,
            font=("Montserrat", 14, "bold"),
            width=150
        )
        label.grid(row=0, column=i, padx=5, pady=5, sticky="w")

    # Load and display data
    with open("data.json", "r") as file:
        data = json.load(file)
        list_anggota = data['list_anggota']

    for i, anggota in enumerate(list_anggota, 1):
        # ID
        customtkinter.CTkLabel(inner_frame, text=str(anggota['id_anggota']), width=50).grid(row=i, column=0, padx=55, pady=2, sticky="w")
        # Username
        customtkinter.CTkLabel(inner_frame, text=anggota['username'], width=150).grid(row=i, column=1, padx=5, pady=2, sticky="w")
        # Nama
        customtkinter.CTkLabel(inner_frame, text=anggota['nama'], width=150).grid(row=i, column=2, padx=5, pady=2, sticky="w")
        # Gender
        customtkinter.CTkLabel(inner_frame, text=anggota['gender'], width=100).grid(row=i, column=3, padx=35, pady=2, sticky="w")
        # Telp
        customtkinter.CTkLabel(inner_frame, text=anggota['telp'], width=150).grid(row=i, column=4, padx=5, pady=2, sticky="w")
        # Alamat
        customtkinter.CTkLabel(inner_frame, text=anggota['alamat'], width=200).grid(row=i, column=5, padx=0, pady=2, sticky="w")
        # Email
        customtkinter.CTkLabel(inner_frame, text=anggota['email'], width=200).grid(row=i, column=6, padx=5, pady=2, sticky="w")

    # Back button
    btn_back = customtkinter.CTkButton(
        container,
        text="← Kembali",
        command=show_crud_anggota,
        width=120,
        height=32,
        corner_radius=8,
        font=("montserrat", 14, "bold"),
        hover_color="#1f538d"
    )
    btn_back.pack(pady=20)
    
# ================================= READ ANGGOTA FUNCTIONS ================================

# ================================= CREATE ANGGOTA FUNCTIONS ==============================

def create_anggota():
    for widget in app.winfo_children():
        widget.pack_forget()

    # Create main container
    container = customtkinter.CTkFrame(app)
    container.pack(fill="both", expand=True, padx=40, pady=40)
    
    # Header
    welcome_label = customtkinter.CTkLabel(
        container, 
        text="Tambahkan Data Anggota",
        font=("Montserrat", 32, "bold"),
        text_color="#1f538d"
    )
    welcome_label.pack(pady=(20, 30))

    # Form container
    form_frame = customtkinter.CTkFrame(container)
    form_frame.pack(fill="x", padx=20)
    form_frame.grid_columnconfigure((0,1), weight=1)

    # Row 1: Username
    label_username = customtkinter.CTkLabel(form_frame, text="Username:", font=("Montserrat", 14))
    label_username.grid(row=2, column=0, padx=10, pady=(5,0), sticky="w")
    entry_username = customtkinter.CTkEntry(form_frame, placeholder_text="Masukkan username", width=250)
    entry_username.grid(row=3, column=0, padx=10, pady=(0,15))
    
    # Row 1: Nama Anggota
    label_nama = customtkinter.CTkLabel(form_frame, text="Nama Anggota:", font=("Montserrat", 14))
    label_nama.grid(row=0, column=0, padx=10, pady=(5,0), sticky="w")
    entry_nama = customtkinter.CTkEntry(form_frame, placeholder_text="Masukkan nama anggota", width=250)
    entry_nama.grid(row=1, column=0, padx=10, pady=(0,15))
    
    # Row 2: Jenis Kelamin
    label_gender = customtkinter.CTkLabel(form_frame, text="Jenis Kelamin:", font=("Montserrat", 14))
    label_gender.grid(row=0, column=1, padx=10, pady=(5,0), sticky="w")
    
    gender_var = customtkinter.StringVar(value="Laki-laki")
    gender_frame = customtkinter.CTkFrame(form_frame)
    gender_frame.grid(row=1, column=1, padx=10, pady=(0,15), sticky="w")
    gender_frame.configure(fg_color="transparent")
    
    radio_laki = customtkinter.CTkRadioButton(
        gender_frame,
        text="Laki-laki",
        variable=gender_var,
        value="Laki-laki",
        font=("Montserrat", 12)
    )
    radio_laki.pack(side="left", padx=(0,20))
    
    radio_perempuan = customtkinter.CTkRadioButton(
        gender_frame,
        text="Perempuan", 
        variable=gender_var,
        value="Perempuan",
        font=("Montserrat", 12)
    )
    radio_perempuan.pack(side="left")

    # Row 2: No Telp
    label_telp = customtkinter.CTkLabel(form_frame, text="Nomor Telp:", font=("Montserrat", 14))
    label_telp.grid(row=2, column=1, padx=10, pady=(5,0), sticky="w")
    entry_telp = customtkinter.CTkEntry(form_frame, placeholder_text="Masukkan nomor telepon", width=250)
    entry_telp.grid(row=3, column=1, padx=10, pady=(0,15))

    # Row 3: Alamat
    label_alamat = customtkinter.CTkLabel(form_frame, text="Alamat:", font=("Montserrat", 14))
    label_alamat.grid(row=4, column=0, padx=10, pady=(5,0), sticky="w")
    entry_alamat = customtkinter.CTkEntry(form_frame, placeholder_text="Masukkan alamat lengkap", width=250)
    entry_alamat.grid(row=5, column=0, padx=10, pady=(0,15))

    # Row 3: Email
    label_email = customtkinter.CTkLabel(form_frame, text="Alamat Email:", font=("Montserrat", 14))
    label_email.grid(row=4, column=1, padx=10, pady=(5,0), sticky="w")
    entry_email = customtkinter.CTkEntry(form_frame, placeholder_text="Masukkan alamat email", width=250)
    entry_email.grid(row=5, column=1, padx=10, pady=(0,15))

    # Buttons container
    button_frame = customtkinter.CTkFrame(container)
    button_frame.pack(fill="x", pady=30)
    button_frame.configure(fg_color="transparent")

    # Submit and Back buttons
    def validate_and_confirm():
        # Check if all fields are filled
        if not entry_username.get() or not entry_nama.get() or \
           not entry_telp.get() or not entry_alamat.get() or not entry_email.get():
            messagebox.showerror("Error", "Semua field harus diisi!")
            return

        # Validate phone number
        if not entry_telp.get().isdigit():
            messagebox.showerror("Error", "Nomor telepon harus berupa angka!")
            return

        # Validate email format
        if '@' not in entry_email.get() or '.' not in entry_email.get():
            messagebox.showerror("Error", "Format email tidak valid!")
            return
        
        # Show confirmation dialog
        if messagebox.askyesno("Konfirmasi", "Apakah anda yakin ingin menambahkan data anggota ini?"):
            submit_anggota(
                entry_username.get(),
                entry_nama.get(),
                gender_var.get(),
                entry_telp.get(), 
                entry_alamat.get(),
                entry_email.get()
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
        command=show_crud_anggota,
        width=200,
        height=40,
        corner_radius=8,
        font=("Montserrat", 14, "bold"),
        fg_color="#666666",
        hover_color="#333333"
    )
    btn_back.pack(side="left", padx=20)

def submit_anggota(username, nama, gender, telp, alamat, email):
    # Read current data
    with open("data.json", "r") as file:
        data = json.load(file)
        list_anggota = data['list_anggota']
        list_buku = data.get('list_buku', [])
        list_peminjaman = data.get('list_peminjaman', [])
        list_pengembalian = data.get('list_pengembalian', [])
        auth = data.get('auth', {})

    # Add new member
    list_anggota.append({
        "id_anggota": len(list_anggota) + 1,
        "username": username,
        "nama": nama,
        "gender": gender,
        "telp": telp,
        "alamat": alamat,
        "email": email
    })

    # Save all data back
    with open("data.json", "w") as file:
        json.dump({
            "auth": auth,
            "list_buku": list_buku,
            "list_peminjaman": list_peminjaman, 
            "list_pengembalian": list_pengembalian,
            "list_anggota": list_anggota
        }, file, indent=4)

    messagebox.showinfo("Success", "Data Anggota Berhasil Ditambahkan")
    show_crud_anggota()
    
# ================================= CREATE ANGGOTA FUNCTIONS ==============================

# ================================= UPDATE ANGGOTA FUNCTIONS ==============================

def update_anggota():
    for widget in app.winfo_children():
        widget.pack_forget()

    # Create main container
    container = customtkinter.CTkFrame(app)
    container.pack(fill="both", expand=True, padx=40, pady=40)
    
    # Header
    welcome_label = customtkinter.CTkLabel(
        container, 
        text="Ubah Data Anggota",  
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
        text="Masukkan ID Anggota yang akan diubah:",
        font=("Montserrat", 16)
    )
    label_id.grid(row=0, column=0, padx=10, pady=(0,10), sticky="w")
    
    entry_id = customtkinter.CTkEntry(
        form_frame,
        placeholder_text="ID Anggota",
        width=300,
        height=40,
        font=("Montserrat", 14)
    )
    entry_id.grid(row=1, column=0, padx=10, pady=(0,20))
    
    btn_submit = customtkinter.CTkButton(
        form_frame,
        text="Submit",
        command=lambda: form_update_anggota(entry_id.get()),
        width=200,
        height=40,
        corner_radius=8,
        font=("Montserrat", 14, "bold"),
        hover_color="#FFA726",
        fg_color="#FF9500"
    )
    btn_submit.grid(row=1, column=1, padx=10, pady=(0,20), sticky="ew")
    
    # Back button
    btn_back = customtkinter.CTkButton(
        container,
        text="← Kembali ke Menu Utama",
        command=show_crud_anggota,
        font=("Montserrat", 14),
        width=200,
        height=40,
        corner_radius=10,
        hover_color="#1f538d",
        fg_color="#333333"
    )
    btn_back.pack(pady=30)

def form_update_anggota(id_anggota):
    try:
        id_anggota = int(id_anggota)
        with open("data.json", "r") as file:
            data = json.load(file)
            list_anggota = data["list_anggota"]
            
        if id_anggota < 1 or id_anggota > len(list_anggota):
            messagebox.showerror("Error", "ID Anggota tidak ditemukan!")
            return
            
        anggota = list_anggota[id_anggota-1]
        
        for widget in app.winfo_children():
            widget.pack_forget()
            
        # Create main container
        container = customtkinter.CTkFrame(app)
        container.pack(fill="both", expand=True, padx=40, pady=40)
        
        # Header
        header_label = customtkinter.CTkLabel(
            container,
            text=f"Update Anggota ID: {id_anggota}",
            font=("Montserrat", 32, "bold"),
            text_color="#1f538d"
        )
        header_label.pack(pady=(20, 30))

        # Form container
        form_frame = customtkinter.CTkFrame(container)
        form_frame.pack(fill="x", padx=20)
        form_frame.grid_columnconfigure((0,1), weight=1)

        # Form fields
        # Username
        label_username = customtkinter.CTkLabel(form_frame, text="Username:", font=("Montserrat", 14))
        label_username.grid(row=0, column=0, padx=10, pady=(5,0), sticky="w")
        entry_username = customtkinter.CTkEntry(form_frame, width=250)
        entry_username.insert(0, anggota["username"])
        entry_username.grid(row=1, column=0, padx=10, pady=(0,15))

        # Nama
        label_nama = customtkinter.CTkLabel(form_frame, text="Nama:", font=("Montserrat", 14))
        label_nama.grid(row=0, column=1, padx=10, pady=(5,0), sticky="w")
        entry_nama = customtkinter.CTkEntry(form_frame, width=250)
        entry_nama.insert(0, anggota["nama"])
        entry_nama.grid(row=1, column=1, padx=10, pady=(0,15))

        # Gender
        label_gender = customtkinter.CTkLabel(form_frame, text="Gender:", font=("Montserrat", 14))
        label_gender.grid(row=2, column=0, padx=10, pady=(5,0), sticky="w")
        
        gender_var = customtkinter.StringVar(value=anggota["gender"])
        gender_frame = customtkinter.CTkFrame(form_frame)
        gender_frame.grid(row=3, column=0, padx=10, pady=(0,15), sticky="w")
        gender_frame.configure(fg_color="transparent")
        
        radio_laki = customtkinter.CTkRadioButton(
            gender_frame,
            text="Laki-laki",
            variable=gender_var,
            value="Laki-laki",
            font=("Montserrat", 12)
        )
        radio_laki.pack(side="left", padx=(0,20))
        
        radio_perempuan = customtkinter.CTkRadioButton(
            gender_frame,
            text="Perempuan",
            variable=gender_var,
            value="Perempuan",
            font=("Montserrat", 12)
        )
        radio_perempuan.pack(side="left")

        # Telepon
        label_telp = customtkinter.CTkLabel(form_frame, text="Telepon:", font=("Montserrat", 14))
        label_telp.grid(row=2, column=1, padx=10, pady=(5,0), sticky="w")
        entry_telp = customtkinter.CTkEntry(form_frame, width=250)
        entry_telp.insert(0, anggota["telp"])
        entry_telp.grid(row=3, column=1, padx=10, pady=(0,15))

        # Alamat
        label_alamat = customtkinter.CTkLabel(form_frame, text="Alamat:", font=("Montserrat", 14))
        label_alamat.grid(row=4, column=0, padx=10, pady=(5,0), sticky="w")
        entry_alamat = customtkinter.CTkEntry(form_frame, width=250)
        entry_alamat.insert(0, anggota["alamat"])
        entry_alamat.grid(row=5, column=0, padx=10, pady=(0,15))

        # Email
        label_email = customtkinter.CTkLabel(form_frame, text="Email:", font=("Montserrat", 14))
        label_email.grid(row=4, column=1, padx=10, pady=(5,0), sticky="w")
        entry_email = customtkinter.CTkEntry(form_frame, width=250)
        entry_email.insert(0, anggota["email"])
        entry_email.grid(row=5, column=1, padx=10, pady=(0,15))

        # Button container
        button_frame = customtkinter.CTkFrame(container)
        button_frame.pack(fill="x", pady=20)
        button_frame.configure(fg_color="transparent")

        def save_changes():
            try:
                # Validate fields
                if not all([entry_username.get(), entry_nama.get(), entry_telp.get(),
                           entry_alamat.get(), entry_email.get()]):
                    messagebox.showerror("Error", "Semua field harus diisi!")
                    return

                # Validate phone number
                if not entry_telp.get().isdigit():
                    messagebox.showerror("Error", "Nomor telepon harus berupa angka!")
                    return

                # Validate email format
                if '@' not in entry_email.get() or '.' not in entry_email.get():
                    messagebox.showerror("Error", "Format email tidak valid!")
                    return

                if messagebox.askyesno("Konfirmasi", "Apakah anda yakin ingin mengubah data anggota ini?"):
                    # Update member data
                    list_anggota[id_anggota-1].update({
                        "username": entry_username.get(),
                        "nama": entry_nama.get(),
                        "gender": gender_var.get(),
                        "telp": entry_telp.get(),
                        "alamat": entry_alamat.get(),
                        "email": entry_email.get()
                    })
                    
                    # Save to file
                    with open("data.json", "w") as file:
                        json.dump(data, file, indent=4)
                    
                    messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui!")
                    show_crud_anggota()
                    
            except ValueError:
                messagebox.showerror("Error", "Terjadi kesalahan saat memproses data!")

        btn_save = customtkinter.CTkButton(
            button_frame,
            text="Simpan Perubahan",
            command=save_changes,
            width=200,
            height=40,
            corner_radius=8,
            font=("Montserrat", 14, "bold"),
            fg_color="#FF9500",
            hover_color="#FFA726"
        )
        btn_save.pack(side="right", padx=20)

        btn_back = customtkinter.CTkButton(
            button_frame,
            text="← Kembali",
            command=update_anggota,
            width=200,
            height=40,
            corner_radius=8,
            font=("Montserrat", 14, "bold"),
            fg_color="#666666",
            hover_color="#333333"
        )
        btn_back.pack(side="left", padx=20)
        
    except ValueError:
        messagebox.showerror("Error", "ID Anggota harus berupa angka!")

# ================================= UPDATE ANGGOTA FUNCTIONS ==============================

# ================================= DELETE ANGGOTA FUNCTIONS ==============================

def delete_anggota():
    for widget in app.winfo_children():
        widget.pack_forget()

    # Create main container
    container = customtkinter.CTkFrame(app)
    container.pack(fill="both", expand=True, padx=40, pady=40)
    
    # Header
    welcome_label = customtkinter.CTkLabel(
        container, 
        text="Hapus Data Anggota",  
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
        text="Masukkan ID Anggota yang akan dihapus:",
        font=("Montserrat", 16)
    )
    label_id.grid(row=0, column=0, padx=10, pady=(0,10), sticky="w")
    
    entry_id = customtkinter.CTkEntry(
        form_frame,
        placeholder_text="ID Anggota",
        width=300,
        height=40,
        font=("Montserrat", 14)
    )
    entry_id.grid(row=1, column=0, padx=10, pady=(0,20))
    
    btn_submit = customtkinter.CTkButton(
        form_frame,
        text="Submit",
        command=lambda: del_anggota(entry_id.get()),
        width=200,
        height=40,
        corner_radius=8,
        font=("Montserrat", 14, "bold"),
        hover_color="#c42b2b",
        fg_color="#d64242"
    )
    btn_submit.grid(row=1, column=1, padx=10, pady=(0,20), sticky="ew")
    
    # Back button
    btn_back = customtkinter.CTkButton(
        container,
        text="← Kembali ke Menu Utama",
        command=show_crud_anggota,
        font=("Montserrat", 14),
        width=200,
        height=40,
        corner_radius=10,
        hover_color="#1f538d",
        fg_color="#333333"
    )
    btn_back.pack(pady=30)

def del_anggota(id_anggota):
    try:
        id_anggota = int(id_anggota)
        with open("data.json", "r") as file:
            data = json.load(file)
            list_anggota = data["list_anggota"]
            list_buku = data.get('list_buku', [])
            list_peminjaman = data.get('list_peminjaman', [])
            list_pengembalian = data.get('list_pengembalian', [])
            auth = data.get('auth', {})
            
        if id_anggota < 1 or id_anggota > len(list_anggota):
            messagebox.showerror("Error", "ID Anggota tidak ditemukan!")
            return
            
        if messagebox.askyesno("Konfirmasi", "Apakah anda yakin ingin menghapus data anggota ini?"):
            # Delete the member
            list_anggota.pop(id_anggota - 1)
            
            # Save all data back
            with open("data.json", "w") as file:
                json.dump({
                    "auth": auth,
                    "list_buku": list_buku,
                    "list_peminjaman": list_peminjaman,
                    "list_pengembalian": list_pengembalian,
                    "list_anggota": list_anggota
                }, file, indent=4)
                
            messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
            show_crud_anggota()
            
    except ValueError:
        messagebox.showerror("Error", "ID Anggota harus berupa angka!")

# ================================= DELETE ANGGOTA FUNCTIONS ==============================

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ANGGOTA AREA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# ================================= MAIN MENU FUNCTIONS ===================================

# run the app
auth()
app.mainloop()

# ================================= MAIN MENU FUNCTIONS ===================================