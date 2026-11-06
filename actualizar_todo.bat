@echo off
chcp 65001 >nul
title Actualizar Plataforma de Tarot (XML + Audios + GitHub)
cls

echo ========================================================================
echo        🔮 ACTUALIZADOR INTELIGENTE - PLATAFORMA DE TAROT
echo ========================================================================
echo.
echo [1/3] Sincronizando archivos XML y calculando duracion de audios...
echo.
python tools/sync_xml_to_db.py

if %ERRORLEVEL% neq 0 (
    echo.
    echo ❌ Ocurrió un error al sincronizar los XML. Revisa la consola arriba.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo ========================================================================
echo [2/3] Sincronizacion local completada con exito.
echo       - Textos actualizados en la base de datos.
echo       - Capitulos de audiolibros listos.
echo       - Duraciones calculadas automaticamente.
echo ========================================================================
echo.
echo ¿Deseas subir estos cambios a tu GitHub ahora mismo? (S/N)
set /p SUBIR="Ingresa S para Si o N para No: "

if /i "%SUBIR%"=="S" (
    echo.
    echo [3/3] Subiendo cambios a GitHub...
    git add .
    git commit -m "Actualizacion de textos XML y audiolibros con capitulos"
    git push origin main
    echo.
    echo ========================================================================
    echo ✅ ¡CAMBIOS SUBIDOS EXITOSAMENTE A GITHUB!
    echo.
    echo Tu plataforma en linea estara actualizada en 1 a 2 minutos en:
    echo 👉 https://angellocp93-blip.github.io/tarot-prueba/
    echo ========================================================================
) else (
    echo.
    echo Cambios guardados localmente. Puedes probar tu web abriendo index.html.
)

echo.
pause

