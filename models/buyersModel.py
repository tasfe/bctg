# -*- coding: utf-8 -*-#
'''
Created on 13-1-12

@author: kom
'''

import traceback
from datetime import *
import sys,hashlib,os
from db.dbModels import *

class buyersModels:
    def __init__(self):
        #self.session = Session()
        self.session = web.ctx
    def getBuyersByCatid(self,cat):
        try:
            buyers = self.session.query(BuyersModel).filter_by(cat3=cat)
            return buyers
        except Exception,e:
            logging.error("getBuyersByCatid,cat:%s  Exception:%s" % (cat,e))
            return -1








