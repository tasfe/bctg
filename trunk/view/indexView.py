'''
Created on 2012-1-17

@author: kom
'''
import web
import os
from common import *

class IndexHandler:
    def GET(self):
        return render('index.html')
