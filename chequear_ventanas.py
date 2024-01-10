import pygetwindow as gw
import time

palabra_clave = "youtube"  # Reemplaza esto con la palabra que estás buscando

while True:
    time.sleep(5)  # Esperar 5 segundos entre cada chequeo
    ventanas_abiertas = gw.getAllTitles()
    for titulo in ventanas_abiertas:
        if palabra_clave.lower() in titulo.lower():  # Comprobación sin diferenciar mayúsculas/minúsculas
            print(f"Encontrada '{palabra_clave}' en la ventana: {titulo}")
