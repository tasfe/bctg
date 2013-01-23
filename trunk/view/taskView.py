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

class tasklistHandler:
    def GET(self):
        data = web.input()
        custid = 1
        tasks =getTaskByCustid(custid)
        return render('tasklist.html',title="tasklist",tasks = tasks)
