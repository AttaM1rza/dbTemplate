# In this file, we'll initialize an engine using create_engine.

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from conf import config

# create database engine
engine = create_engine(
    f"postgresql+psycopg2://{config['database']['username']}:{config['database']['password']}@{config['database']['host']}:{config['database']['port']}/{config['database']['name']}",
    echo=True
)



# create a connection with the database
def create_connection():
    return engine.connect()
