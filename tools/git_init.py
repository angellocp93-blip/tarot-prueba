import subprocess
import os

git_exe = os.path.expandvars(r"%LOCALAPPDATA%\Programs\MinGit\cmd\git.exe")

def run_git(args):
    res = subprocess.run([git_exe] + args, capture_output=True, text=True)
    print(f"$ git {' '.join(args)}")
    if res.stdout:
        print(res.stdout.strip())
    if res.stderr:
        print(res.stderr.strip())
    return res

# 1. git init
run_git(["init", "-b", "main"])

# 2. check git config
user_name = run_git(["config", "user.name"])
if not user_name.stdout.strip():
    run_git(["config", "user.name", "Tarot Explorer"])
    run_git(["config", "user.email", "tarot@example.com"])

# 3. git add .
run_git(["add", "."])

# 4. git status
run_git(["status"])

# 5. git commit
run_git(["commit", "-m", "Initial commit: 78 Mapas Visuales del Tarot - Plataforma de Estudio y Práctica"])

