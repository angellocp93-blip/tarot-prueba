@echo off
title Subir 78 Mapas del Tarot a GitHub
cls
echo ========================================================================
echo       SUBIR PLATAFORMA DE TAROT A TU GITHUB (Y GITHUB PAGES)
echo ========================================================================
echo.
echo Paso 1: Crea un repositorio vacio en https://github.com/new
echo         (Por ejemplo llamado: tarot-mapas)
echo.
echo Paso 2: Copia el enlace HTTPS de tu repositorio de GitHub.
echo.
echo ========================================================================
set /p REPO_URL="Pega aqui la URL de tu repositorio de GitHub: "

if "%REPO_URL%"=="" (
    echo No ingresaste ninguna URL. Operacion cancelada.
    pause
    exit /b
)

echo.
echo Conectando con tu repositorio y subiendo archivos...
echo.

python tools\push_to_github.py "%REPO_URL%"

echo.
echo ========================================================================
echo Para activar tu web publica gratuita en tu celular:
echo 1. Ve a tu repositorio en GitHub
echo 2. Entra en "Settings" -> "Pages"
echo 3. En "Branch" selecciona "main" y "/ (root)", y dale a "Save"
echo 4. En 1 minuto tendras tu web lista en: https://TU-USUARIO.github.io/tu-repo/
echo ========================================================================
pause

