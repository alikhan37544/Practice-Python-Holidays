import http.server
import socketserver

# Set the port number for the server
PORT = 8000

# Define the request handler class
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=".", **kwargs)

# Create the server
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Server started on port {PORT}")
    # Start the server
    httpd.serve_forever()
