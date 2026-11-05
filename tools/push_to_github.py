import sys
import subprocess
import os

if len(sys.argv) < 2:
    print("Error: Debes proporcionar la URL del repositorio.")
    sys.exit(1)

repo_url = sys.argv[1].strip()

# Path to git
git_exe = os.path.expandvars(r"%LOCALAPPDATA%\Programs\MinGit\cmd\git.exe")
if not os.path.exists(git_exe):
    git_exe = "git"

print(f"Configurando origen remoto: {repo_url}")

# Check existing remote
remotes = subprocess.run([git_exe, "remote"], capture_output=True, text=True).stdout

if "origin" in remotes:
    subprocess.run([git_exe, "remote", "set-url", "origin", repo_url])
else:
    subprocess.run([git_exe, "remote", "add", "origin", repo_url])

print("Subiendo rama 'main' a GitHub...")
res = subprocess.run([git_exe, "push", "-u", "origin", "main"])

if res.returncode == 0:
    print("\n✓ ¡Proyecto subido con éxito a GitHub!")
else:
    print("\nSi GitHub te solicita iniciar sesión, introduce tus credenciales o Personal Access Token.")

