
from spotspot import app


@app.route('/')
@app.route('/address/')
def enterAddress():
    return "This page will let the user enter their address"

@app.route('/map/user/')
def showMap():
    return "This page will show a map with the user"

@app.route('/lot/<int:lot_id>/')
@app.route('/lot/<int:lot_id>/info/')
def lotInfo(lot_id):
    return "This page will show info about a lot with an ID of %r" % lot_id
