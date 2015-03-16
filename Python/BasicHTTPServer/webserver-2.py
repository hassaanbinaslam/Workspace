from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

"""
Basic HTTP Webserver

Implemented URL routing and HTML views for GET request.
Returns error when requested view is not found.
"""

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/hello'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = '<html><body>Hello World!</body></html>'
            self.wfile.write(message)
            return
        if self.path.endswith('/yellow'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = '<html><body>Yellow World!</body></html>'
            self.wfile.write(message)
            return
        else:
            self.send_error(404, 'File Not Found: '+self.path)

def run():
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, RequestHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    httpd.serve_forever()

if __name__ == '__main__':
    run()