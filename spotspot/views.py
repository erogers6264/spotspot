from spotspot import app
from flask import render_template, request, redirect, url_for

from flask_googlemaps import Map

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Lot, Base 

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


@app.route('/lots/new/', methods=['GET', 'POST'])
def newLot():
    if request.method == 'POST':
        newLot = Lot(address=request.form['address'],
            image_url=request.form['image_url'],
            capacity=request.form['capacity']
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

@app.route('/')
@app.route('/destination/')
def enterAddress():
    return render_template('enteraddress.html')


@app.route('/lots/<int:lot_id>/')
@app.route('/lots/<int:lot_id>/info/')
def lotInfo(lot_id):
    return render_template('lotinfo.html')
