import tkinter as tk
from tkinter import messagebox

# import data buku dari data.json
import json
with open("data.json", "r") as file:
    data = json.load(file)
    list_buku = data['list_buku']
    list_peminjaman = data['list_peminjaman']
    list_pengembalian = data['list_pengembalian']


# tampilkan Ucapan selamat datang dan List Menu yang tersedia dan Tombol untuk memilih menu yang diinginkan menggunakan gui tkinter
root = tk.Tk()
root.title("Perpustakaan")
root.geometry("1080x720")

# Label
label = tk.Label(root, text="Selamat Datang di Perpustakaan", font=("montserrat", 24, "bold"), justify="center")
label.pack(pady=120)

space = tk.Label(root, text="")
space.pack()

def show_crud_buku(): 

    label = tk.Label(text="CRUD Buku: ", font=("Arial", 20, "bold"), justify="center", padx=0, pady=-40)
    label.pack(pady=10)

   
    button.pack_forget()

    space = tk.Label(root, text="")
    space.pack()

    button2_1 = tk.Button(root, text="Lihat Buku", font=("arial", 14), width=20)
    button2_1.pack(pady=5)

    button2_2 = tk.Button(root, text="Tambah Buku", font=("arial", 14), width=20)
    button2_2.pack(pady=5)

    button2_3 = tk.Button(root, text="Edit Buku", font=("arial", 14), width=20)
    button2_3.pack(pady=5)

    button2_4 = tk.Button(root, text="Hapus Buku", font=("arial", 14), width=20)
    button2_4.pack(pady=5)

    button2_5 = tk.Button(root, text="← Kembali", font=("arial", 14), width=20)
    button2_5.pack(pady=30)

       
def show_menu():
    label.config(text="Pilih Menu :")
    label.pack(pady=120)

    button.pack_forget()

    space = tk.Label(root, text="")
    space.pack()

    button1_1 = tk.Button(root, text="CRUD Buku", font=("arial", 14), command=show_crud_buku, width=24, justify="center")
    button1_1.pack(pady=5)

    button1_2 = tk.Button(root, text="CRUD Peminjaman Buku", font=("arial", 14), width=24)
    button1_2.pack(pady=5)

    button1_3 = tk.Button(root, text="CRUD Pengembalian Buku", font=("arial", 14), width=24)
    button1_3.pack(pady=5)

    button1_4 = tk.Button(root, text="← Kembali", font=("arial", 14), width=17)
    button1_4.pack(pady=40)


def show_crud_peminjaman():
    print("CRUD Peminjaman Buku :")

# tombol untuk masuk ke menu
button = tk.Button(root, text="Masuk", font=("arial", 18), command=show_menu, width=20)
button.pack()

root.mainloop()

# 

