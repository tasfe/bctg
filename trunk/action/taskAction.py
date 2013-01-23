# -*- coding: utf-8 -*-#
'''
Created on 13-1-21

@author: kom
'''


from models.taskModel import *

taskmodels = taskModels()

def addTask(args):
    if not args.has_key("custid"):
        return 0
    custid = args["custid"]
    catid = args["cat3"]
    category_level = 3
    title = args["title"]
    content = args["content"]
    print content
    return taskmodels.addTask(custid,catid,category_level,title,content)

def getTaskByCustid(custid):
    return taskmodels.getTask(custid)