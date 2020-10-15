#####################################################
# Import dependencies
#####################################################
import numpy as np
import os

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#####################################################
# Setup Database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)
print(Base.classes.keys())

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station

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
        f"Precipitation >> /api/v1.0/precipitation<br/>"
        f"Stations >> /api/v1.0/stations<br/>"
        f"Tobs>> /api/v1.0/tobs<br/>"
        f"/api/v1.0/start date yyyy-mm-dd<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():

    # open communication session with database
    session = Session(engine)

    # query measurement.date and measurement.prcp for last year
    results = session.query(measurement.date,measurement.prcp).filter(measurement.date >= "2016-08-23")
    
    # close the session
    session.close()
    
    # create dictionary using 'date' as the key and 'prcp' as the value
    measurement_data = []
    for dates in results:
        measurement_dict = {}
        measurement_dict["date"] = dates.date
        measurement_dict["prcp"] = dates.prcp
        measurement_data.append(measurement_dict)

    mesurement[row.date - row.prcp


    # Return the JSON representation of your dictionary
    return jsonify(measurement_data)

@app.route("/api/v1.0/stations")
def stations():
    
    # open communication session with database
    session = Session(engine)

    # query measurement.date and measurement.prcp for last year
    stations = session.query(measurement.station,func.count(measurement.station)).group_by(measurement.station).order_by(func.count(measurement.station).desc()).all()
    
    # close the session
    session.close()

    # station_data = []
    # for station in stations:
    #     stations_dict = {}
    #     stations_dict["name"] = station[0]
    #     stations_dict["count"] = station[1]
    #     station_data.append(stations_dict)

    # Return the JSON representation of your dictionary
    #return jsonify(station_data)
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():

# open communication session with database
    session = Session(engine)

    # query measurement.date and measurement.prcp for last year
    stations = session.query(measurement.station,func.count(measurement.station)).group_by(measurement.station).order_by(func.count(measurement.station).desc())
    
    # close the session
    session.close()



@app.route("/api/v1.0/temps/<start>")
@app.route("/api/v1.0/temps/<start>/<end>")

def start(start_date=None, end_date=None)

    ## open communication session with database
    session = Session(engine)
    
    # query measurement.date and measurement.prcp for last year
    if end_input:
        results - session.query(func.min(Measuremrnt.tobs).label("min", func.max(Measurement.tobs).label("max"), func.avg(Measurement.tobs).label("avg")/
        .filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    
    else:
        results - session.query(func.min(Measuremrnt.tobs).label("min", func.max(Measurement.tobs).label("max"), func.avg(Measurement.tobs).label("avg")/
        .filter(Measurement.date >= start_date).all()

    # close the session
    session.close()

    # for loop to pull results for dates provided
    temp_data = []
    for result in results:
        temp_dict = {}
        temp_dict["min"] = result.min
        temp_dict["max"] = result.max
        temp_dict["avg"] = result.avg


if __name__ == "__main__":
    app.run(debug=True)
