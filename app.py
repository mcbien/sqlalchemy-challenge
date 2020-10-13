#####################################################
# Import dependencies
#####################################################
from flask import Flask
import numpy as np
import os

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify

#####################################################
# Create an app
#####################################################
app = Flask(__name__)

#####################################################
# Create routes
#####################################################
@app.route("/")
def home():
    print("available routes")
    return (
        f"Bien: sqlalchemy-challenge<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start date yyyy-mm-dd<br/>"
        f"/api/v1.0/end date yyyy-mm-dd<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    print("test")
    return("Precipitation")

@app.route("/api/v1.0/stations")
def stations():
    print("test")
    return("Stations")

@app.route("/api/v1.0/tobs")
def tobs():
    print("test")
    return("tobs")

# @app.route("/api/v1.0/<start>")

#     print("test")
#     return("test")

# @app.route("/api/v1.0/<start>/<end>")

#     print("test")
#     return("test")

if __name__ == "__main__":
    app.run(debug=True)
