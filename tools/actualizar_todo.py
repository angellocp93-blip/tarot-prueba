# -*- coding: utf-8 -*-
"""
Script de Actualización Completa para la Plataforma de Tarot
1. Sincroniza todos los archivos XML en 'cartas_xml/'.
2. Calcula automáticamente la duración de los audios en 'assets/audio/'.
3. Procesa capítulos con marcas de tiempo.
4. Genera data/tarot_database.json y data/tarot_database.js.
5. Sube automáticamente a GitHub si el usuario lo confirma.
"""

import sys
import os
import subprocess

# Forzar codificación UTF-8 en consola de Windows
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def run():
    print("=" * 72)
    print("        🔮 ACTUALIZADOR COMPLETO - PLATAFORMA DE TAROT")
    print("=" * 72)
    print()
    print("[1/3] Sincronizando archivos XML y calculando duracion de audios...")
    print()

    # Importar y ejecutar sincronizador
    tools_dir = os.path.dirname(os.path.abspath(__file__))
    if tools_dir not in sys.path:
        sys.path.insert(0, tools_dir)

    try:
        import sync_xml_to_db
        sync_xml_to_db.sync()
    except Exception as e:
        print(f"❌ Error durante la sincronización: {e}")
        return

    print()
    print("=" * 72)
    print("[2/3] Sincronización completada con éxito.")
    print("      ✓ Textos de las cartas actualizados.")
    print("      ✓ Duraciones de audio calculadas automáticamente.")
    print("      ✓ Capítulos y marcas de tiempo preparados.")
    print("=" * 72)
    print()

    # Verificar estado de git
    try:
        status_res = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, encoding="utf-8")
        has_changes = bool(status_res.stdout.strip())
    except Exception:
        has_changes = True

    if not has_changes:
        print("ℹ️ No hay cambios pendientes por subir a GitHub. Todo está al día.")
        print()
        print("Puedes revisar tu plataforma en vivo en:")
        print("👉 https://angellocp93-blip.github.io/tarot-prueba/")
        return

    # Preguntar al usuario si desea subir a GitHub
    try:
        resp = input("¿Deseas subir estos cambios a tu GitHub ahora mismo? (S/N) [S]: ").strip()
    except EOFError:
        resp = "S"

    if resp == "" or resp.upper() in ["S", "SI", "Y", "YES"]:
        print()
        print("[3/3] Subiendo cambios a GitHub...")
        try:
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "Actualizacion de textos XML y audiolibros con capitulos"], check=True)
            push_res = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True, encoding="utf-8")
            if push_res.returncode == 0:
                print()
                print("=" * 72)
                print(" ✅ ¡CAMBIOS SUBIDOS EXITOSAMENTE A GITHUB!")
                print()
                print(" Tu plataforma en línea estará lista en 1 a 2 minutos en:")
                print(" 👉 https://angellocp93-blip.github.io/tarot-prueba/")
                print()
                print(" 💡 Consejo: Si abres la página y aún ves la versión previa,")
                print("    presiona Ctrl + F5 o abre una pestaña de Incógnito.")
                print("=" * 72)
            else:
                print(f"⚠️ Aviso al hacer push: {push_res.stderr or push_res.stdout}")
        except subprocess.CalledProcessError as err:
            print(f"❌ Error al ejecutar comando git: {err}")
    else:
        print()
        print("ℹ️ Cambios guardados localmente. Puedes probar abriendo index.html.")

if __name__ == '__main__':
    run()

