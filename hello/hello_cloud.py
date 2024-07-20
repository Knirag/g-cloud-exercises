#!/usr/bin/env python3

import http.server
import socketserver
import sys

# Default port
PORT = 8000

# Check if a port number is provided as an argument
if len(sys.argv) > 1:
    try:
        PORT = int(sys.argv[1])
    except ValueError:
        print("Invalid port number. Using default port 8000.")
        
class HelloHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, Cloud!")

# Create an object of the above class
handler_object = HelloHandler

# Create a TCP socket to listen on the specified port
with socketserver.TCPServer(("", PORT), handler_object) as httpd:
    print(f"Serving HTTP on port {PORT}...")
    httpd.serve_forever()

