import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode

def generate_qr():
    text = entry.get()
    if not text.strip():
        messagebox.showerror("Error", "Please enter some text to generate QR code.")
        return
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="blue", back_color="yellow")
    
    file_name = "qr_code.png"
    img.save(file_name)
    
    img = Image.open(file_name)
    img = img.resize((200, 200)) 
    img_tk = ImageTk.PhotoImage(img)
    
    qr_label.config(image=img_tk)
    qr_label.image = img_tk  
    
    entry.delete(0, tk.END)

window = tk.Tk()
window.title("QR Code Generator")
window.geometry("400x500")
window.configure(bg="#1e1e1e")

label = tk.Label(window, text="Enter text or URL:", fg="white", bg="#1e1e1e", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(window, width=40, font=("Arial", 12), borderwidth=2, relief="solid")
entry.pack(pady=10)

generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr, 
                            font=("Arial", 12), fg="white", bg="#007bff", 
                            activebackground="#0056b3", activeforeground="white", relief="raised")
generate_button.pack(pady=20)

qr_label = tk.Label(window, bg="#1e1e1e")
qr_label.pack(pady=10)

window.mainloop()
