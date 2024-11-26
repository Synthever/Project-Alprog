import tkinter as tk
from tkinter import messagebox

# import data buku dari data.json
import json
with open("data.json", "r") as file:
    data = json.load(file)
    list_buku = data['list_buku']
    list_peminjaman = data['list_peminjaman']
    list_pengembalian = data['list_pengembalian']

# Fungsi untuk berpindah dari laman menu ke laman CRUD Buku dengan background biru muda
def show_crud_buku():
    page_crud_buku = tk.Frame(root, bg="white")
    page_crud_buku.place(relwidth=1, relheight=1)

    label.config(text="CRUD Buku :", font=("montserrat", 20, "bold"))
    label.pack()

    button.pack_forget()

    space = tk.Label(root, text="")
    space.pack()

    button2_1 = tk.Button(root, text="Lihat Buku", width=20)
    button2_1.pack(pady=5)

    button2_2 = tk.Button(root, text="Tambah Buku", width=20)
    button2_2.pack(pady=5)

    button2_3 = tk.Button(root, text="Edit Buku", width=20)
    button2_3.pack(pady=5)

    button2_4 = tk.Button(root, text="Hapus Buku", width=20)
    button2_4.pack(pady=5)

# Fungsi untuk berpindah dari laman selamat datang ke laman menu dengan background putih
def show_menu():
    page_menu= tk.Frame(root, bg="white")
    page_menu.place(relwidth=1, relheight=1)
    
    label.config(text="Pilih Menu :", font=("montserrat", 20, "bold"))
    label.pack()

    button.pack_forget()

    space = tk.Label(root, text="")
    space.pack()

    button1_1 = tk.Button(root, text="CRUD Buku", command=show_crud_buku, width=20)
    button1_1.pack(pady=5)

    button1_2 = tk.Button(root, text="CRUD Peminjaman Buku", width=20)
    button1_2.pack(pady=5)

# tampilkan Ucapan selamat datang dan List Menu yang tersedia dan Tombol untuk memilih menu yang diinginkan menggunakan gui tkinter
root = tk.Tk()
root.title("Perpustakaan")
root.geometry("1080x720")

# Label
label = tk.Label(root, text="Selamat Datang di Perpustakaan", font=("montserrat", 24, "bold"), justify="center")
label.pack(pady=120)

space = tk.Label(root, text="")
space.pack()

button = tk.Button(root, text="Masuk", command=show_menu, width=20)
button.pack(pady=5)

root.mainloop()


