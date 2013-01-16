# -*- coding: utf-8 -*-#
'''
Created on 13-1-12

@author: kom
'''
from common import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DateTime,Text

Base = declarative_base()
class BuyersModel(Base):
    __tablename__ = 'buyers'
    id = Column(Integer, primary_key=True)
    user_id= Column(String(10),doc="taobao user_id")
    email = Column(String(40),doc="email address")
    cat1 = Column(Integer(5),doc="一级类目")
    cat2 = Column(Integer(5),doc="二级类目")
    cat3 = Column(Integer(5),doc="三级类目")
    buyDate = Column(DateTime,doc="buy item date")
    updateDate = Column(DateTime,doc="insert date")
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
    catid= Column(Integer(5),doc="类目id")
    catName = Column(String(40),doc="类目名称")
    parent_id = Column(Integer(5),doc="父类目id")
    category_level = Column(Integer(2),doc="类目级别")
    status = Column(Integer(2),doc="状态")
    sort_order = Column(Integer(5),doc="排序值")
    sort_type = Column(Integer(2),doc="排序类型")
    updateDate = Column(DateTime,doc="更新时间")
    def __init__(self, catid=0, catName='', parent_id=0,category_level=0,status=0,sort_order=0,sort_type=0,updateDate=''):
        self.catid = catid
        self.catName = catName
        self.parent_id = parent_id
        self.category_level = category_level
        self.status = status
        self.sort_order = sort_order
        self.sort_type = sort_type
        self.updateDate = updateDate


class TaskModel(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    custid = Column(Integer, doc="发起任务的用户id")
    catid= Column(Integer(5),doc="发送目标的类目id")
    category_level = Column(Integer(2),doc="类目级别")
    content = Column(Text,doc="发送内容")
    status = Column(Integer(2),doc="状态：0，未发送；1，发送成功；2，开始发送；3，发送失败")
    def __init__(self, custid=0,catid=0,category_level=0,content="",status=-1):
        self.custid = custid
        self.Catid = Catid
        self.category_level = category_level
        self.content = content
        self.status = status

metadata = Base.metadata

if __name__ == "__main__":
    metadata.create_all(engine)
    print "over"
