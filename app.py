from http.server import BaseHTTPRequestHandler, HTTPServer

class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello from Jenkins + GitHub 🚀")

server = HTTPServer(("0.0.0.0", 5000), AppHandler)
print("App running on port 5000")
server.serve_forever()
