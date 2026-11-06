@echo off
title Actualizar Plataforma de Tarot
cd /d "%~dp0"
python tools\actualizar_todo.py
echo.
pause
