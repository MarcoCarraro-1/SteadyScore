import tkinter as tk
from tkinter import messagebox

def greet_user():
    messagebox.showinfo("Benvenuto", "Ciao e benvenuto al progetto!")

# Creazione della finestra principale
root = tk.Tk()
root.title("Benvenuto")

# Dimensioni della finestra
root.geometry("300x200")

# Etichetta
label = tk.Label(root, text="Benvenuto!", font=("Arial", 16))
label.pack(pady=20)

# Bottone per il saluto
button = tk.Button(root, text="Saluta", command=greet_user)
button.pack(pady=10)

# Avvio dell'app
root.mainloop()