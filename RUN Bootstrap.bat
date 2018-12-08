::Este archivo bach levanta el servicio flask app.py automaticamente
echo off
cls
::color 8f
::mode con:cols=110 lines=30
for /f "delims=[] tokens=2" %%a in ('ping -4 -n 1 %ComputerName% ^| findstr [') do set NetworkIP=%%a
for /f %%a in ('powershell Invoke-RestMethod api.ipify.org') do set PublicIP=%%a
TITLE App:  -  ( IP Privada: %NetworkIP% )  -  ( IP Publica: %PublicIP% )
cd C:\eclipse-workspace\Trivia_Con_Bootstrap\src
set FLASK_APP=app.py
set FLASK_ENV=development
cls
python -m flask run --host=0.0.0.0