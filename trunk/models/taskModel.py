# -*- coding: utf-8 -*-#
'''
Created on 13-1-12

@author: kom
'''

import traceback
from datetime import *
import sys,hashlib,os
from db.dbModels import *

class taskModels:
    def __init__(self):
        self.db = web.ctx.orm

    def getTask(self,cust_id):
        try:
            tasks = self.db.query(TaskModel).filter_by(custid=cust_id).all()
            return tasks
        except Exception,e:
            logging.error("taskModels.getTask,cust_id:%s  Exception:%s" % (cust_id,e))
            logging.exception(e)
            return 0

    def getNextTodoTask(self):
        try:
            task = self.db.query(TaskModel).filter_by(status=0).orderby(id).first()
            return task
        except Exception,e:
            logging.error("taskModels.getNextTodoTask  Exception:%s" % (e))
            return 0

    def addTask(self,cust_id,cat_id,category_level,title,content,status = 0):
        try:
            newTask = TaskModel(custid=cust_id,
                                catid=cat_id,
                                category_level=category_level,
                                title = title,
                                content=content,
                                status=status)
            self.db.add(newTask)
            self.db.commit()
            return 1
        except Exception,e:
            logging.error("taskModels.addTask  Exception:%s" % (e))
            logging.exception(e)
            return 0
