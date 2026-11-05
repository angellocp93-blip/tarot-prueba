import http.server
import socketserver
import webbrowser
import socket
import json
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connecting to a public UDP address doesn't send packets, but resolves the local interface IP
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

LOCAL_IP = get_local_ip()

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == '/api/info':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            data = {
                "local_ip": LOCAL_IP,
                "port": PORT,
                "mobile_url": f"http://{LOCAL_IP}:{PORT}"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))
            return
        super().do_GET()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def run_server():
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        local_url = f"http://localhost:{PORT}"
        mobile_url = f"http://{LOCAL_IP}:{PORT}"
        print("=" * 72)
        print(" ✨ 78 MAPAS VISUALES DEL TAROT - PLATAFORMA PERSONAL ACTIVA ✨")
        print("=" * 72)
        print(f" 💻 En tu PC abre:")
        print(f"    -> {local_url}")
        print()
        print(f" 📱 En tu CELULAR (Android o iPhone en la misma red Wi-Fi) abre:")
        print(f"    -> {mobile_url}")
        print("=" * 72)
        print(" Presiona Ctrl + C en esta ventana para detener el servidor.")
        print("=" * 72)
        
        # Open in default browser on PC
        try:
            webbrowser.open(local_url)
        except Exception:
            pass

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n Servidor detenido. ¡Hasta pronto!")
            sys.exit(0)

if __name__ == '__main__':
    run_server()
