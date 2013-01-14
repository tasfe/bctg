# -*- coding: utf-8 -*-#
'''
Created on 2012-1-14

@author: kom
'''

import web
from urls import url
import os
from view import *
from common import *

app = web.application(url, globals())
app.add_processor(load_sqla)


if __name__ == "__main__":
    if os.name == "posix":
        web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
        #web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()