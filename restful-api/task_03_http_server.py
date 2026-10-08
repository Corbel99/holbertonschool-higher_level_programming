#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPI(BaseHTTPRequestHandler):
    """Handle HTTP GET requests for the simple API."""

    def do_GET(self):
        """Handle GET requests for the API endpoints."""
        if self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode())
        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        elif self.path == "/status":
            self.send_response(200)
            self.end_headers()
            self.wfile.write("OK".encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write("Endpoint not found".encode())


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), SimpleAPI)
    server.serve_forever()
