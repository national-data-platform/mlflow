from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from socketserver import ThreadingMixIn

host = "0.0.0.0"
port = 5004

response = {
    "issuer": "http://fake-keycloak:5004",
    "authorization_endpoint": "http://fake-keycloak:5004/protocol/openid-connect/auth",
    "token_endpoint": "http://fake-keycloak:5004/protocol/openid-connect/token",
    "introspection_endpoint": "http://fake-keycloak:5004/protocol/openid-connect/token/introspect",
    "userinfo_endpoint": "http://fake-keycloak:5004/protocol/openid-connect/userinfo",
    "end_session_endpoint": "http://fake-keycloak:5004/protocol/openid-connect/logout",
    "jwks_uri": "http://fake-keycloak:5004/protocol/openid-connect/certs",
    "check_session_iframe": "http://fake-keycloak:5004/protocol/openid-connect/login-status-iframe.html"
}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(json.dumps(response).encode()))


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


server = ThreadedHTTPServer((host, port), Handler)
print('starting..')
server.serve_forever()
