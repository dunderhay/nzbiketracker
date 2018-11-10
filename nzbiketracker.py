import flask

import database

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/api/update')
def update():
    bike_locations = []

    for location in database.Location.select():
        bike_locations.append([location.latitude, location.longitude])

    return flask.jsonify(bike_locations)
