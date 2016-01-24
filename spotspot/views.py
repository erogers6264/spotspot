from spotspot import app
from flask import render_template, request

from flask_googlemaps import Map

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Lot, Destination, Base 

engine = create_engine('sqlite:///lots.db')
Base.metadata.bind = engine

DBsession = sessionmaker(bind=engine)
session = DBsession()


@app.route('/map/<destination_id>/')
def showMap(destination_id):
    # creating a map in the view
    lots = []

    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    return render_template('map.html', mymap=mymap, sndmap=sndmap)


@app.route('/lots/')
def allLots():
    lots = session.query(Lot).all()
    return render_template('lots.html', lots=lots)


@app.route('/lots/new/')
def newLot():
    return render_template('newlot.html')

@app.route('/lots/<int:lot_id>/edit/')
def editLot(lot_id):
    return render_template('editlot.html')

@app.route('/lots/<int:lot_id>/delete/')
def deleteLot(lot_id):
    return render_template('deletelot.html')

@app.route('/')
@app.route('/destination/')
def enterAddress():
    return render_template('enteraddress.html')


@app.route('/lots/<int:lot_id>/')
@app.route('/lots/<int:lot_id>/info/')
def lotInfo(lot_id):
	return render_template('lotinfo.html')



