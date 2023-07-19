import platform
from http.server import HTTPServer, SimpleHTTPRequestHandler

print(platform.node() + ".local")
httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
