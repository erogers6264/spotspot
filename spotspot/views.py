
from spotspot import app


@app.route('/')
@app.route('/destination/')
def enterAddress():
    return "This page will let the user enter their address"

@app.route('/map/<destination_id>/')
def showMap(destination_id):
    return "This page will show a map with the user surrounded by lots"

@app.route('/lots/')
def allLots():
    return "This page will show all lots in a nice list view"

@app.route('/lot/<int:lot_id>/')
@app.route('/lot/<int:lot_id>/info/')
def lotInfo(lot_id):
    return "This page will show info about a lot with an ID of %r" % lot_id

@app.route('/lot/new/')
def newLot():
    return "This page will let you add a new parking lot"


