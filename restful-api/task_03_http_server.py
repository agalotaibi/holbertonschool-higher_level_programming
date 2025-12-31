"""
A simple HTTP API using Python's standard http.server module.

This script sets up a basic web server that handles GET requests
and returns either text or JSON data depending on the endpoint.
"""


import http.server
import json
import socketserver


PORT = 8000

class run(http.server.BaseHTTPRequestHandler):
    """
    Starts the HTTP server on port 8000.

    Args:
        server_class: The class to use for the server (default: HTTPServer).
        handler_class: The class to handle requests (default: BaseHTTPRequestHandler).
    """

    def do_GET(self):
        """
        Handles HTTP GET requests.

        Routes the request based on the path:
        - '/'     : Returns a text greeting.
        - '/data' : Returns a JSON dataset.
        - Other   : Returns a 404 Not Found error.
        """

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

with socketserver.TCPServer(("", PORT),run ) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
