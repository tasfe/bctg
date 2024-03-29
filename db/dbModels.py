# -*- coding: utf-8 -*-#
'''
Created on 13-1-12

@author: kom
'''
from common import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

Base = declarative_base()

class customerModel(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    nick = Column(String(40),doc="nick")
    type = Column(Integer(2),doc="用户类型")
    def __init__(self, nick="",type=0):
        self.nick = nick
        self.type = type

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
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    catid= Column(Integer(5),doc="类目id")
    catName = Column(String(40),doc="类目名称")
    parentid = Column(Integer(5),doc="父类目id")
    categorylevel = Column(Integer(2),doc="类目级别")
    status = Column(Integer(2),doc="状态")
    sortorder = Column(Integer(5),doc="排序值")
    sorttype = Column(Integer(2),doc="排序类型")
    updateDate = Column(TIMESTAMP,nullable=False, default=func.current_timestamp(),doc="时间")
    def __init__(self, catid=0, catName='', parentid=0,categorylevel=0,status=0,sortorder=0,sorttype=0,updateDate=''):
        self.catid = catid
        self.catName = catName
        self.parentid = parentid
        self.categorylevel = categorylevel
        self.status = status
        self.sortorder = sortorder
        self.sorttype = sorttype
        self.updateDate = updateDate


class TaskModel(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    custid = Column(Integer, doc="发起任务的用户id")
    catid= Column(Integer(5),doc="发送目标的类目id")
    category_level = Column(Integer(2),doc="类目级别")
    title = Column(String(40),doc="标题")
    content = Column(Text,doc="发送内容")
    status = Column(Integer(2),doc="状态：0，未发送；1，发送成功；2，开始发送；3，发送失败")
    createDate = Column(TIMESTAMP,nullable=False, default=func.current_timestamp(),doc="建立时间")
    updateDate = Column(DateTime,doc="更新时间")
    def __init__(self, custid=0,catid=0,category_level=0,title="",content="",status=0,createDate="",updateDate=""):
        self.custid = custid
        self.catid = catid
        self.category_level = category_level
        self.title = title
        self.content = content
        self.status = status
        self.createDate = createDate
        self.updateDate = updateDate

metadata = Base.metadata

if __name__ == "__main__":
    metadata.create_all(engine)
    print "over"
