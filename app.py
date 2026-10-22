import os
import http.server
import socketserver

# Obtener variables de entorno para desarrollo/producción
PORT = int(os.environ.get("PORT", 5000))
ENVIRONMENT = os.environ.get("ENVIRONMENT", "desarrollo")

class NuevaNetHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Endpoint de verificación de salud (Healthcheck)
        if self.path == '/health':
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            response = f'{{"status": "UP", "company": "NuevaNet", "environment": "{ENVIRONMENT}"}}'
            self.wfile.write(response.encode('utf-8'))
            return

        # Interfaz web principal de NuevaNet
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        badge_color = "#28a745" if ENVIRONMENT.lower() == "produccion" else "#ffc107"
        
        html = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>NuevaNet - Gestión de Aplicaciones</title>
            <style>
                body {{ font-family: Arial, sans-serif; background-color: #f4f6f9; margin: 0; padding: 40px; text-align: center; }}
                .card {{ background: white; max-width: 600px; margin: 0 auto; padding: 30px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }}
                h1 {{ color: #003366; }}
                .badge {{ background-color: {badge_color}; color: white; padding: 6px 12px; border-radius: 4px; font-weight: bold; text-transform: uppercase; }}
                .status {{ margin-top: 20px; color: #2e7d32; font-size: 18px; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🌐 NuevaNet Tecnologías</h1>
                <h2>Sistema de Gestión de Aplicaciones</h2>
                <p><strong>Entorno de Ejecución:</strong> <span class="badge">{ENVIRONMENT}</span></p>
                <div class="status">
                    <p>✔ Servicio operativo y optimizado en contenedor.</p>
                </div>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode('utf-8'))

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), NuevaNetHandler) as httpd:
        print(f"Servidor NuevaNet iniciado en el puerto {PORT} | Entorno: {ENVIRONMENT}")
        httpd.serve_forever()