from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, World!")

if __name__ == "__main__":
    HTTPServer(('0.0.0.0', 8000), SimpleHandler).serve_forever()
