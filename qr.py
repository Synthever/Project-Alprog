import tkinter as tk
from tkinter import messagebox
import customtkinter
import qrcode

# Generate QR Code and save png
def generate():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(entry.get())
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr.png")
    img.show()

# Custom Tkinter System Setting
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Window or frame
app = customtkinter.CTk()
app.geometry("450x150")
app.title("QR Code Generator")

# Spacing no text
spacing = customtkinter.CTkLabel(app, text="")
spacing.pack()

# Label futuristic style
label = customtkinter.CTkLabel(app, text="Enter text to generate QR Code:")
label.pack()

# Entry box
entry = customtkinter.CTkEntry(app)
entry.pack()

# Spacing no text
spacing = customtkinter.CTkLabel(app, text="")
spacing.pack()

# Button
button = customtkinter.CTkButton(app, text="Generate", command=generate)
button.pack()

# run the app
app.mainloop()