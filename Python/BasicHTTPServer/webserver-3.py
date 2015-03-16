from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import cgi

"""
Basic HTTP Webserver

Implemented POST request handler
Implemented form POST and GET
"""

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/hello'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            output = ""
            output += "<html><body>"
            output += "<h1>Hello!</h1>"
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'>
                            <h2>What would you like me to say?</h2>
                            <input name="message" type="text" >
                            <input type="submit" value="Submit">
                        </form>'''
            output += "</body></html>"
            self.wfile.write(output)
            return
        else:
            self.send_error(404, 'File Not Found: ' + self.path)

    def do_POST(self):
        self.send_response(301)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            fields = cgi.parse_multipart(self.rfile, pdict)
            messagecontent = fields.get('message')
        output = ""
        output += "<html><body>"
        output += " <h2> Okay, how about this: </h2>"
        output += "<h1> %s </h1>" % messagecontent[0]
        output += '''<form method='POST' enctype='multipart/form-data' action='/hello'>
                        <h2>What would you like me to say?</h2>
                        <input name="message" type="text" >
                        <input type="submit" value="Submit">
                    </form>'''
        output += "</body></html>"
        self.wfile.write(output)
        return

def run():
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, RequestHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    httpd.serve_forever()

if __name__ == '__main__':
    run()