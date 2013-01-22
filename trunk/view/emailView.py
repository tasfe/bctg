'''
Created on 2012-1-17

@author: kom
'''
import web
import os
import json
from common import *
from action.buyersAction import *
from action.taskAction import *
from action.catAction import *

class EmailHandler:
    def GET(self):
        cat1 = getCatsbyParentid(0)
        return render('email.html',title="email",cat1 = cat1)


class DoMailHandler:
    def POST(self):
        data = web.input()
        data["custid"] = 1
        addTask(data)
        return render('email.html')

class taskHandler:
    def GET(self):
        data=web.data()
        return "ok"

class catHandler:
    def GET(self):
        data=web.input()
        return json.dumps(getCatsbyParentid(data.catid))


class getbuyernumHandler:
    def GET(self):
        data=web.input()
        return getBuyersNumBycatid(data)