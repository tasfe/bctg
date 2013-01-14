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
        self.session = Session()

    def getTask(self,cust_id):
        try:
            tasks = self.session.query(TaskModel).filter_by(custid=cust_id)
            return tasks
        except Exception,e:
            logging.error("taskModels.getTask,cust_id:%s  Exception:%s" % (cust_id,e))
            return 0

    def getNextTodoTask(self):
        try:
            task = self.session.query(TaskModel).filter_by(status=0).orderby(id).first()
            return task
        except Exception,e:
            logging.error("taskModels.getNextTodoTask  Exception:%s" % (e))
            return 0
