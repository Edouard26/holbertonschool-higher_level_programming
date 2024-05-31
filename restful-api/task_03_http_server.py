from __future__ import annotations

import http.server
import json


class SimpleRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data':
            data = {
                'name': 'John'
                'age': '30'
                'city': 'New York'
            }

            json_data = json.dumps(data)

            self.send_response(200)

            self.send_header('Content-type', 'application/json')
            self.end_headers()

            self.wfile.write(json_data.encode('utf-8'))
        elif self.path == '/status':

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')

        else:

            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Endpoint not found')


if __name__ == '__main__':

    server_adress = ('', 8000)
    httpd = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)

    print('Starting server on port 8000...')
    httpd.serve_forever()
