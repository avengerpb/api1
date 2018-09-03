import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

Session = sessionmaker()
engine = create_engine('mysql://avengerpb:datvip12@api1.clqiyfvnms6u.eu-west-1.rds.amazonaws.com/api1')
Session.configure(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)

class User_Info(Base):
    __tablename__ = 'userInfo'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_street_name = Column(String(250))
    user_street_number = Column(String(250))
    user_post_code = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
def init_db():
    Base.metadata.create_all(engine)
