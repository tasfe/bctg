# -*- coding: utf-8 -*-#
'''
Created on 13-1-15

@author: kom
'''

from models.buyersModel import *

buyersmodels = buyersModels()

def getBuyersNumBycatid(cat):
    if cat.has_key("cat3"):
        cat = cat["cat3"]
    elif cat.has_key("cat2"):
        cat = cat["cat2"]
    elif cat.has_key("cat1"):
        cat = cat["cat1"]
    else:
        return 0
    if True:#todo 增加memcache
        buyers = buyersmodels.getBuyersByCatid(cat)
        if buyers == -1:
            return -1
        return len(buyers)


if __name__ == '__main__':
    print getBuyersNumBycatid(cat3=1234)