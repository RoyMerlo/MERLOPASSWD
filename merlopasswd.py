import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class MerloPasswd:
    def __init__(self, root):
        self.root = root
        self.root.title("MerloPass-wd")
        self.root.geometry("400x300")
        self.root.configure(bg="black")

        title = tk.Label(root, text="MerloPass-wd", font=("Helvetica", 24, "bold"), fg="yellow", bg="black")
        title.pack(pady=10)

        subtitle = tk.Label(root, text="Generatore di password", font=("Helvetica", 12), fg="yellow", bg="black")
        subtitle.pack()

        self.output = tk.Entry(root, font=("Helvetica", 14), justify="center")
        self.output.pack(pady=20)

        button_frame = tk.Frame(root, bg="black")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Password Complessa", command=self.generate_complex, bg="yellow", fg="black").grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Password Semplice", command=self.generate_simple, bg="yellow", fg="black").grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Copia", command=self.copy_password, bg="gray", fg="white").grid(row=1, column=0, columnspan=2, pady=10)

        footer = tk.Label(root, text="Creato da Roy Merlo", font=("Helvetica", 10), bg="black", fg="gray")
        footer.pack(side="bottom", pady=5)

    def generate_complex(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(16))
        self.output.delete(0, tk.END)
        self.output.insert(0, password)

    def generate_simple(self):
        characters = string.ascii_lowercase + string.digits
        password = ''.join(random.choice(characters) for _ in range(8))
        self.output.delete(0, tk.END)
        self.output.insert(0, password)

    def copy_password(self):
        password = self.output.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copiato", "Password copiata negli appunti!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MerloPasswd(root)
    root.mainloop()


