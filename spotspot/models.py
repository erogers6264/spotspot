import sys

from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

associate_lot_destination = Table('lot_destination', Base.metadata,
    Column('lot_id', Integer, ForeignKey('lot.id')),
    Column('destination_id', Integer, ForeignKey('destination.id'))
)

class Lot(Base):
	"""A simple classsc for the parking lots in the database"""
	
	__tablename__ = 'lot'
	id = Column(Integer, primary_key = True)
	address = Column(String)
	capacity = Column(Integer)
	fill_level = Column(Integer, default = 0)
	image_url = Column(String)
	destinations = relationship("Destination",
		secondary = associate_lot_destination,
		back_populates = 'lots')


class Destination(Base):
	"""Information about a space"""
	
	__tablename__ = 'destination'
	id = Column(Integer, primary_key = True)
	name = Column(String)
	address = Column(String)
	lots = relationship("Lot",
		secondary = associate_lot_destination,
		back_populates = 'destinations') 

engine = create_engine('sqlite:///lots.db')
Base.metadata.create_all(engine)