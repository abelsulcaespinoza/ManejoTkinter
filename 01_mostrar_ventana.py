import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Redimensionar la ventana
ventana.geometry("900x600")

# Modificar el título de la ventana
ventana.title("Mi primera ventana con Tkinter")

# Evitar el cambio de tamaño de la ventana
ventana.resizable(False, False)

# Color de la ventana
ventana.configure(background="#1d2d44")

# Hacer visible la ventana
ventana.mainloop()