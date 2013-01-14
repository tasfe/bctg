'''
Created on 2011-12-7

@author: kom
'''
import os
import logging


setting=dict(
    apiurl = 'http://gw.api.tbsandbox.com/router/rest',
    appkey = '12443826',
    secretKey = 'sandboxec3eed15f5f56fe3a35441592',
    gatewayUrl = 'http://gw.api.tbsandbox.com/router/rest',
    format = "json",
    template_path = os.path.join(os.path.dirname(__file__), "template"),
    static_path = os.path.join(os.path.dirname(__file__), "static"),
    debug=True,
    )

dbname="mysql"
dbuser="bctg"
dbpassword="bctg"
dbaddress="127.0.0.1"
dbport="8306"
dbdbase="bctg"
Echo=True



BASE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),os.pardir,"log")
logFormat = '[%(asctime)s] %(levelname)s %(message)s'
logFilename = 'vitem.log'
logLevel = logging.INFO
#logging.basicConfig(level=logLevel,
#    format=logFormat,
#    filename=os.path.join(BASE_PATH,logFilename),
#    filemode='a')
#Session = sessionmaker(bind=engine)