# create a simple web server

import SimpleHTTPServer, SocketServer

evtHandler = SimpleHTTPServer.SimpleHTTPRequestHandler

myHTTPserver = SocketServer.TCPServer(("0.0.0.0", 8080), evtHandler)

print "My sever is now running. (CTRL + C to stop)..."

myHTTPserver.serve_forever()
