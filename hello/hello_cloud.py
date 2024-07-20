import http.server
import socketserver

PORT = 8000

class HelloHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, Cloud!")

# Create an object of the above class
handler_object = HelloHandler

# Create a TCP socket to listen on port 8000
with socketserver.TCPServer(("", PORT), handler_object) as httpd:
    print(f"Serving HTTP on port {PORT}...")
    httpd.serve_forever()

