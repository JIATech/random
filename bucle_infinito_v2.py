import tkinter as tk
import random

def smooth_move_button(new_x, new_y, steps=600):
    # Calcular el paso de movimiento en x e y
    step_x = (new_x - button.winfo_x()) / steps
    step_y = (new_y - button.winfo_y()) / steps

    for step in range(steps):
        # Programar cada paso de la animación
        top_level_window.after(step * 2, lambda step=step: button.place(x=max(0, min(top_level_window.winfo_width() - button.winfo_width(), button.winfo_x() + step * step_x)),
                                                                       y=max(0, min(top_level_window.winfo_height() - button.winfo_height(), button.winfo_y() + step * step_y))))

def move_button(event):
    button_x = button.winfo_x()
    button_y = button.winfo_y()
    button_width = button.winfo_width()
    button_height = button.winfo_height()

    cursor_x, cursor_y = event.x, event.y

    distance = ((button_x + button_width/2 - cursor_x)**2 + (button_y + button_height/2 - cursor_y)**2)**0.5

    if distance < 100:
        button_width = button.winfo_width()
        button_height = button.winfo_height()

        # Calcular una nueva posición aleatoria dentro de los límites de la ventana
        new_x = random.randint(0, top_level_window.winfo_width() - button_width)
        new_y = random.randint(0, top_level_window.winfo_height() - button_height)

        smooth_move_button(new_x, new_y)

def create_top_level_window():
    global top_level_window, window_position, button

    top_level_window = tk.Toplevel()
    top_level_window.title("Mensaje Importante")

    width = random.randint(1000, 1280)
    height = random.randint(200, 720)
    x_position = int((width/2) - (width/2))
    y_position = int((height/2) - (height/2))
    window_position = f"+{x_position}+{y_position}"
    top_level_window.geometry(f"{width}x{height}")
    top_level_window.configure(bg="black")

    top_level_window.resizable(False, False)
    top_level_window.attributes('-topmost', True)
    top_level_window.attributes('-toolwindow', True)

    tk.Label(top_level_window, text="No debo dejar la PC desbloqueada", font=("Helvetica", 48), bg="black", fg="white").pack(expand=True)
    
    # Crear el botón y luego posicionarlo
    button = tk.Button(top_level_window, text="Aceptar", command=lambda: [top_level_window.destroy(), on_close()])
    button.place(x=200, y=200)

    top_level_window.protocol("WM_DELETE_WINDOW", lambda: [top_level_window.destroy(), on_close()])

    top_level_window.bind('<Configure>', on_move)
    top_level_window.bind('<Unmap>', on_minimize)
    top_level_window.bind('<Motion>', move_button)

def on_move(event):
    global window_position
    current_position = f"+{top_level_window.winfo_x()}+{top_level_window.winfo_y()}"
    if current_position != window_position:
        # Si la ventana se ha movido, restablece su posición a la anterior
        top_level_window.geometry(window_position)

def on_minimize(event):
    top_level_window.deiconify()  # Restaurar la ventana si se minimiza

def on_close():
    root.after(100, create_top_level_window)

# Ventana principal de Tkinter, oculta
root = tk.Tk()
root.withdraw()

# Crear la primera ventana Toplevel
create_top_level_window()

root.mainloop()