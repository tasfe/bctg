# -*- coding: utf-8 -*-#
'''
Created on 13-1-17

@author: kom
'''

import traceback
from datetime import *
import sys,hashlib,os
from db.dbModels import *

class catModels:
    def __init__(self):
    #self.session = Session()
        self.session = web.ctx.orm

    def getCatsbyParentid(self,parent_id):
        try:
            cats = self.session.query(CatModel).find(parentid = parent_id)
            return cats
        except Exception,e:
            logging.error("getCatsbyParentid,parent_id:%s  Exception:%s" % (parent_id,e))
            return -1