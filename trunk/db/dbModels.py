# -*- coding: utf-8 -*-#
'''
Created on 13-1-12

@author: kom
'''

Base = declarative_base()
class BuyersModel(Base):
    __tablename__ = 'buyers'
    id = Column(Integer, primary_key=True)
    user_id= Column(String(10))
    email = Column(String(40))
    cat1 = Column(Integer(5))
    cat2 = Column(Integer(5))
    cat3 = Column(Integer(5))
    buyDate = Column(DateTime)
    updateDate = Column(DateTime)
    def __init__(self, user_id=0, email='', cat1='',cat2='',cat3='',buyDate='',updateDate=''):
        self.user_id = user_id
        self.email = email
        self.cat1 = cat1
        self.cat2 = cat2
        self.cat3 = cat3
        self.buyDate = buyDate
        self.updateDate = updateDate

class CatModel(Base):
    __tablename__ = 'Cat'
    id = Column(Integer, primary_key=True)
    catid= Column(Integer(5))
    catName = Column(String(40))
    cat1 = Column(Integer(5))
    cat2 = Column(Integer(5))
    cat3 = Column(Integer(5))
    buyDate = Column(DateTime)
    updateDate = Column(DateTime)
    def __init__(self, user_id=0, email='', cat1='',cat2='',cat3='',buyDate='',updateDate=''):
        self.user_id = user_id
        self.email = email
        self.cat1 = cat1
        self.cat2 = cat2
        self.cat3 = cat3
        self.buyDate = buyDate
        self.updateDate = updateDate

metadata = Base.metadata


if __name__ == "__main__":
    metadata.create_all(engine)
    print "over"
