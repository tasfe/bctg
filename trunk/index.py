# -*- coding: utf-8 -*-#
'''
Created on 2012-1-13

@author: kom
'''

import tornado
import tornado.web
import tornado.ioloop
from tornado.httpserver import HTTPServer
from view import *
import urls, settings


class Application(tornado.web.Application):
    def __init__(self):
        self.settings= settings.setting
        self.handlers= urls.handler
        tornado.web.Application.__init__(self, self.handlers, **self.settings)

def Main(port):
    app = Application()
    #tornado.options.parse_command_line()
    #print 'start up ......'
    server = HTTPServer(app)
    server.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    #Main(int(sys.argv[1]))
    Main(8888)