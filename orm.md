 engine = create_engine('sqlite:///:memory:', echo=True)
echo 通过 python标准的logging模块实现，激活日志 ，会记录所有的SQL

Engine, 核心访问数据的接口，通过调整dialect,
适配不同的数据库和dbpai,
Lazy Connecting
当调用 connect或者第一次调用execute是才会连接数据库

orm 不会直接使用 Engine


使用Declarative系统 声明 mapping   类与数据库表的映射
需要一个declarative_base
>>> from sqlalchemy.ext.declarative import declarative_base
>>> Base = declarative_base()
Base 只需要一个实例
自定义类继承Base即可
>>> from sqlalchemy import Column, Integer, String
>>> class User(Base):
...     __tablename__ = 'users'
...
...     id = Column(Integer, primary_key=True)
...     name = Column(String(50))  
...     fullname = Column(String)
...     password = Column(String)
...
...     def __repr__(self):
...        return "<User(name='%s', fullname='%s', password='%s')>" % (
...                             self.name, self.fullname, self.password)


可以指定varchar的长度，Base.metadata.create_all(engine)创建schema。

创建回话 session
>>> from sqlalchemy.orm import sessionmaker
>>> Session = sessionmaker(bind=engine)
>>> session = Session()
当使用session的时候 从池中取出一个连接


