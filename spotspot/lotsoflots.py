from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from models import Lot, Base
 
engine = create_engine('sqlite:///lots.db')
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()

lot1 = Lot(address='825 W E St, San Diego, CA 92101', capacity=300,
	image_url='http://i.imgur.com/5X77r1i.png')
session.add(lot1)
session.commit()

lot1 = Lot(address='60 W Harbor Dr, San Diego, CA 92101', capacity=50,
	image_url='http://i.imgur.com/5X77r1i.png')
session.add(lot1)
session.commit()

lot1 = Lot(address='ADDRESS HERE', capacity=500,
	image_url='http://i.imgur.com/5X77r1i.png')
session.add(lot1)
session.commit()

lot1 = Lot(address='ADDRESS HERE', capacity=255,
	image_url='http://i.imgur.com/5X77r1i.png')
session.add(lot1)
session.commit()

lot1 = Lot(address='ADDRESS HERE', capacity=476,
	image_url='http://i.imgur.com/5X77r1i.png')
session.add(lot1)
session.commit()

lot1 = Lot(address='ADDRESS HERE', capacity=123,
	image_url='http://i.imgur.com/5X77r1i.png')
session.add(lot1)
session.commit()

print "Added lots!"
