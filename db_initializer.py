# In this file, we'll initialize an engine using create_engine.

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from base_conf import DATABASE

# create database engine
engine = create_engine(
    "postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}".format(
        db_username=DATABASE['USERNAME'],
        db_password=DATABASE['PASSWORD'],
        db_host=DATABASE['HOST'],
        db_port=DATABASE['PORT'],
        db_name=DATABASE['NAME']
    ),
    echo=True
)

#connection = engine.connect()
base = declarative_base()

class schedule(base):
    __tablename__ = 'schedule'
    id = Column(Integer, primary_key=True)
    time = Column(String)
    monday = Column(String)
    tuesday = Column(String)
    wednesday = Column(String)
    thursday = Column(String)
    friday = Column(String)
    saturday = Column(String)

base.metadata.create_all(engine)


# create a connection with the database
def create_connection():
    return engine.connect()
