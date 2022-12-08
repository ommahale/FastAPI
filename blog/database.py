from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABSE_URL='sqlite:///./blog.db'

engine=create_engine(url=SQLALCHEMY_DATABSE_URL,connect_args={'check_same_thread':False})

session=sessionmaker(bind=engine,autocommit=False,autoflush=False)

Base=declarative_base()