import tkinter as tk
import random


def create_window():
    window = tk.Tk()
    window.title("Mensaje Importante")
    # Generar dimensiones aleatorias para la ventana
    width = random.randint(300, 1920)  # Ancho aleatorio entre 300 y 1920
    height = random.randint(200, 1080)  # Altura aleatoria entre 200 y 1080
    window.geometry(f"{width}x{height}")  # Establecer tamaño de la ventana
    window.configure(bg="black")  # Establecer color de fondo

    tk.Label(window, text="No debo dejar la PC desbloqueada", font=("Helvetica", 16), bg="black", fg="white").pack(expand=True)
    tk.Button(window, text="Aceptar", command=window.destroy).pack()
    window.mainloop()

def schedule_new_window(root, interval=1500):
    root.after(interval, lambda: create_window())
    root.after(interval, lambda: schedule_new_window(root, interval))

# Crear una ventana raíz para manejar el temporizador
root = tk.Tk()
root.withdraw()  # Oculta la ventana raíz
schedule_new_window(root)
root.mainloop()
