from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

"""
Basic HTTP Webserver

The first class 'HTTPServer' creates HTTP socket and listens to it. 
Any request that comes to it, it dispatches it to the handler .

The second class 'BaseHTTPRequestHandler' is used to handle the HTTP requests that
arrive at the server. By itself, it cannot respond to any actual HTTP request; it
must be subclassed to handle each request method (GET or POST). The handler will
parse the request and header, then call a method specific to request type.

As we have not implemented any request handler, our server will generate built in error response saying Error Code=501.
Unsupported method (GET) has been called
"""

def run():
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, BaseHTTPRequestHandler)
    httpd.serve_forever()
    
if __name__ == '__main__':
    run()