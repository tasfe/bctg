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

if dbname == 'sqlite':
    engine = create_engine(dbname+':///'+dbaddress, echo=Echo)
else:
    engine = create_engine(dbname+'://'+dbuser+':'+dbpassword+'@'+dbaddress+':'+dbport+'/'+dbdbase+'?charset=utf8',echo=Echo)

Session = sessionmaker(bind=engine)