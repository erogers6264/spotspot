import sys

from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Lot(Base):
	"""A simple class for the parking lots in the database"""
	
	__tablename__ = 'lot'
	id = Column(Integer, primary_key = True)
	address = Column(String)
	lat = Column(Float)
	lng = Column(Float)
	capacity = Column(Integer)
	fill_level = Column(Integer, default = 0)
	image_url = Column(String)

class Destination(Base):
	"""To store address queries made against the program"""

	__tablename__ = 'address'
	id = Column(Integer, primary_key = True)
	address = Column(String)
	lat = Column(Float)
	lng = Column(Float)

engine = create_engine('sqlite:///lots.db')
Base.metadata.create_all(engine)