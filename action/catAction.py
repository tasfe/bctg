# -*- coding: utf-8 -*-#
'''
Created on 13-1-17

@author: kom
'''

from models.catModel import *


catmodels = catModels()
def getCatsbyParentid(parent_id = 0):
    if True:#todo 增加memcache
        cats = catmodels.getCatsbyParentid(cat)
        if cats == -1:
            return {}
        return cats