'''
Created on 2012-1-17

@author: kom
'''
import web
import os
from common import *


class EmailHandler:
    def GET(self):
        return render('email.html')

class startTaskHandler:
    def POST(self):
        data = web.data()
        print data
        return render('email.html')

class taskHandler:
    def GET(self):
        data=web.data()
