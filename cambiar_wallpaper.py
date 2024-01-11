import ctypes
import getpass

def change_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 0x0014
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

# Get the username of the current Windows session
username = getpass.getuser()

# Usage example
image_path = r'C:\Users\{username}\Pictures\wallpaper.jpg'.format(username=username)
change_wallpaper(image_path)
