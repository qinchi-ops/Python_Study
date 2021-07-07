#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

from http.server import HTTPServer, CGIHTTPRequestHandler
port = 80
httpd = HTTPServer(('',port), CGIHTTPRequestHandler)
print('Starting simple httpd on port: ' + str(httpd.server_port))
httpd.serve_forever()