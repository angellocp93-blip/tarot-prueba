@echo off
title Sincronizador de Textos XML - Tarot
cls
echo ========================================================================
echo   SINCRONIZADOR DE CARTAS XML -> PLATAFORMA DE TAROT
echo ========================================================================
echo.
echo Leyendo archivos XML modificados en la carpeta 'cartas_xml'...
echo Actualizando data/tarot_database.json y data/tarot_database.js...
echo.
python tools/sync_xml_to_db.py
echo.
echo ========================================================================
echo Sincronizacion finalizada. Puedes refrescar tu navegador (Ctrl + F5).
echo ========================================================================
pause

