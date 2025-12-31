"""
A simple HTTP API using Python's standard http.server module.

This script sets up a basic web server that handles GET requests
and returns either text or JSON data depending on the endpoint.
"""


import http.server
import json

def run(server_class=http.server.HTTPServer, handler_class=http.server.BaseHTTPRequestHandler):
    """
    Starts the HTTP server on port 8000.

    Args:
        server_class: The class to use for the server (default: HTTPServer).
        handler_class: The class to handle requests (default: BaseHTTPRequestHandler).
    """
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

class Handler(http.server.BaseHTTPRequestHandler):
    """
    Custom HTTP request handler to manage API endpoints and routing.
    """

    def do_GET(self):
        """
        Handles HTTP GET requests.

        Routes the request based on the path:
        - '/'     : Returns a text greeting.
        - '/data' : Returns a JSON dataset.
        - Other   : Returns a 404 Not Found error.
        """
        if self.path == '/':
            self.send_response(200)
            self.end_headers()
            message = "Hello, this is a simple API!"
            self.wfile.write(message.encode())
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json_message = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.wfile.write(json_message.encode())
        else:
            self.send_error(404, "Endpoint not found")


if __name__ == '__main__':
    run(handler_class=Handler)
