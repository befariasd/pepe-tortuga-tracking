from http.server import BaseHTTPRequestHandler, HTTPServer

HTML = """<html><head><meta charset="utf-8"><title>Pepe Tortuga - Rastreo</title></head><body>
<h1>Transportes Pepe Tortuga S.A.</h1><h2>Panel de rastreo de flota</h2>
<table border="1" cellpadding="6"><tr><th>Camión</th><th>Ruta</th><th>Estado</th></tr>
<tr><td>TRK-001</td><td>Santiago - Valparaíso</td><td>En ruta</td></tr>
<tr><td>TRK-002</td><td>Santiago - Concepción</td><td>Detenido</td></tr>
<tr><td>TRK-003</td><td>Santiago - La Serena</td><td>En ruta</td></tr>
</table></body></html>"""

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML.encode())

HTTPServer(("0.0.0.0", 5000), H).serve_forever()
