# -*- coding: utf-8 -*-# 
'''
Created on 2012-1-13

@author: kom
'''

import web
from view import *

url = ("/", "view.indexView.IndexHandler",
       "/email", "view.emailView.EmailHandler",
       "/domail","view.emailView.DoMailHandler",
       "/startTask","view.emailView.startTaskHandler",
       "/test","view.testView.testHandler",
       "/cat","view.emailView.catHandler",
    )
