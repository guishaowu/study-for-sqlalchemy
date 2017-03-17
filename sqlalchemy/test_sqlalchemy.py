from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
Session = sessionmaker()
Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                            self.name, self.fullname, self.password)



Base.metadata.create_all(engine)
session = Session(bind=engine)
ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
session.add(ed_user)
our_user = session.query(User).filter_by(name='ed').first()
print(our_user)
