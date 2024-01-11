
@echo off
set "F=%cd%"
set "source=%F%\cambiar_wallpaper.exe"
set "destination=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\"

xcopy /Y "%source%" "%destination%"