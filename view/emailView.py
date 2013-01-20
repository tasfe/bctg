'''
Created on 2012-1-17

@author: kom
'''
import web
import os
from common import *
from action.buyersAction import *

class EmailHandler:
    def GET(self):
        return render('email.html',title="email")


class DoMailHandler:
    def POST(self):
        data = web.data()
        print data
        return render('email.html')

class taskHandler:
    def GET(self):
        data=web.data()
        return "ok"

class catHandler:
    def GET(self):
        data=web.input()
        return getcatByid(data.catid)
