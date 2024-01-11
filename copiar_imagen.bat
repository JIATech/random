@echo off
set "F=%cd%"
set "source=%F%\wallpaper.jpg"
set "destination=C:\Users\%USERNAME%\Pictures\"

xcopy /Y "%source%" "%destination%"

