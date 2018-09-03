import os
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .models import *

Session = sessionmaker()
engine = create_engine('mysql://avengerpb:datvip12@api1.clqiyfvnms6u.eu-west-1.rds.amazonaws.com/api1')
Session.configure(bind=engine)
session = Session()


def init_db():
    Base.metadata.create_all(engine)
