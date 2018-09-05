from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    password =  Column(String(250), nullable=False)

class User_Info(Base):
    __tablename__ = 'user_info'
    id = Column(Integer, primary_key=True)
    user_email = Column(String(250), nullable=False)
    user_phone = Column(String(250))
    user_address = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Note(Base):
    __tablename__ = 'note'
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    image_url = Column(String(250))
    created_at = Column(DateTime)
    update_at = Column(DateTime)
    status = Column(Integer, nullable=False, server_default='0')
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
