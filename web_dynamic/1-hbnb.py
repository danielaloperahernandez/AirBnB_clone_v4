#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template, url_for
import uuid
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def closedb(foo):
    """Closes db session"""
    storage.close()


@app.route('/1-hbnb', strict_slashes=False)
def hbnb_filters():
    """Route /hbnb_filters"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template('1-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())


if __name__ == '__main__':
    storage.reload()
    app.run("0.0.0.0", 5000)