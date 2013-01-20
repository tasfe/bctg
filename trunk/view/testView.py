# -*- coding: utf-8 -*-#
'''
Created on 13-1-19

@author: kom
'''

import web
import os
from common import *

class testHandler:
    def GET(self):
        return render('test.html',title="test")