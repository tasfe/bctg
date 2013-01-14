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
        self.session = Session()

    def getBuyersByCatid(self,cat):
        try:
            buyers = self.session.query(BuyersModel).filter_by(cat3=cat)
            return buyers
        except Exception,e:
            logging.error("getBuyersByCatid,cat:%s  Exception:%s" % (cat,rights,e))
            return 0


    def getBuyersNumBycatid(self,**cat):
        if cat.has_key("cat3"):
            cat = cat["cat3"]
        elif cat.has_key("cat2"):
            cat = cat["cat2"]
        elif cat.has_key("cat1"):
            cat = cat["cat1"]
        else:
            return 0

        if True:#todo 增加memcache
            buyersNum = len(self.getBuyersByCatid(cat))
        return buyersNum





