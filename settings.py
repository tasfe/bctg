'''
Created on 2011-12-7

@author: kom
'''
import os


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


#Session = sessionmaker(bind=engine)