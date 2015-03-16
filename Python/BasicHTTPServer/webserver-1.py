from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

"""
Basic HTTP Webserver

Implemented GET request handler.
Whatever GET request is send to the server, it replies back with 'Hello World' textual message.
"""
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message = 'Hello World!'
        self.wfile.write(message)
        return

def run():
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, RequestHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    httpd.serve_forever()
    
if __name__ == '__main__':
    run()