from spotspot import app
from flask import render_template, request, redirect, url_for

from flask_googlemaps import Map

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Lot, Base, Destination

from spothelper import getCoordinates

engine = create_engine('sqlite:///lots.db')
Base.metadata.bind = engine

DBsession = sessionmaker(bind=engine)
session = DBsession()


@app.route('/map/<destination_id>')
def showMap(destination_id):
    destination = session.query(Destination).filter_by(id=destination_id).one()
    # creating a map in the view
    lots = session.query(Lot).all()
    markers = {'http://maps.google.com/mapfiles/ms/icons/blue-dot.png':[(lot.lat, lot.lng)] for lot in lots}

    mymap = Map(
        identifier="destination",
        lat=destination.lat,
        lng=destination.lng,
        markers=markers
    )
    return render_template('map.html', mymap=mymap)


@app.route('/lots/')
def allLots():
    lots = session.query(Lot).all()
    return render_template('lots.html', lots=lots)


@app.route('/lots/new/', methods=['GET', 'POST'])
def newLot():
    if request.method == 'POST':
        address = request.form['address']
        coords = getCoordinates(address)
        newLot = Lot(address=address,
            image_url=request.form['image_url'],
            capacity=request.form['capacity'],
            lat=coords[0],
            lng=coords[1]
            )

        session.add(newLot)
        session.commit()
        return redirect(url_for('allLots'))
    else:
        return render_template('newlot.html')


@app.route('/lots/<int:lot_id>/edit/', methods=['GET', 'POST'])
def editLot(lot_id):
    if request.method == 'POST':
        edited_lot = session.query(Lot).filter_by(id=lot_id).one()
        if request.form['address']:
            edited_lot.address = request.form['address']
            coords = getCoordinates(edited_lot.address)
            edited_lot.lat, edited_lot.lng = coords[0], coords[1]
        if request.form['image_url']:
            edited_lot.image_url = request.form['image_url']
        if request.form['capacity']:
            edited_lot.capacity = request.form['capacity']
        session.add(edited_lot)
        session.commit()
        return redirect(url_for('allLots'))
    else:
        lot = session.query(Lot).filter_by(id=lot_id).one()
        return render_template('editlot.html', lot=lot)


@app.route('/lots/<int:lot_id>/delete/', methods=['GET', 'POST'])
def deleteLot(lot_id):
    if request.method == 'POST':
        lot_to_delete = session.query(Lot).filter_by(id=lot_id).one()
        session.delete(lot_to_delete)
        session.commit()
        return redirect(url_for('allLots'))
    else:
        lot = session.query(Lot).filter_by(id=lot_id).one()
        return render_template('deletelot.html', lot=lot)


@app.route('/', methods=['GET', 'POST'])
@app.route('/destination/', methods=['GET', 'POST'])
def enterAddress():
    if request.method == 'POST':
        destination = Destination(address=request.form['destination'])
        coords = getCoordinates(destination.address)
        destination.lat, destination.lng = coords[0], coords[1]
        session.add(destination)
        session.commit()
        return redirect(url_for('showMap', destination_id=destination.id))
    else:
        return render_template('enteraddress.html')


@app.route('/lots/<int:lot_id>/')
@app.route('/lots/<int:lot_id>/info/')
def lotInfo(lot_id):
    lot = session.query(Lot).filter_by(id=lot_id).one()
    return render_template('lotinfo.html', lot=lot)
