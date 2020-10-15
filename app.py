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
        f"Bien: sqlalchemy-challenge<br/><br/><br/>"
        f"Available Routes:<br/><br/>"
        f"Precipitation: /api/v1.0/precipitation<br/><br/>"
        f"Stations: /api/v1.0/stations<br/><br/>"
        f"Tobs: /api/v1.0/tobs<br/><br/>"
        f"Start Date End Date /api/v1.0/start_date/end_date<br/><br/>"
        f"Note: Date format is YYY-MM-DD"
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
        measurement_dict[dates.date] = dates.prcp
        # measurement_dict["date"] = dates.date
        # measurement_dict["prcp"] = dates.prcp
        measurement_data.append(measurement_dict)

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

    # query tobs for the most active station for the past year
    one_year_tobs = session.query(measurement.tobs).filter(measurement.date >= "2016-08-23").filter(measurement.station == "USC00519281").all()

    # close session
    session.close()

    # return the JSON representation of dictionary
    return jsonify(one_year_tobs)


@app.route('/api/v1.0/<start_date>')
@app.route('/api/v1.0/<start_date>/<end_date>')

def start(start_date=None, end_date=None):

    # open cummunication session with database
    session = Session(engine)

    # When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
    if end_date is None:
        results = session.query(func.min(measurement.tobs).label("TMIN"), func.max(measurement.tobs).label("TMAX"), func.avg(measurement.tobs).label("TAVG")).filter(measurement.date >= start_date).all()

    else:
        results = session.query(func.min(measurement.tobs).label("TMIN"), func.max(measurement.tobs).label("TMAX"), func.avg(measurement.tobs).label("TAVG")).filter(measurement.date >= start_date).filter(measurement.date <= end_date).all()

    #close the session
    session.close()

    temp_data = []
    for temp in results:
        temp_dict = {}
        temp_dict["TMIN"] = temp.TMIN
        temp_dict["TMAX"] = temp.TMAX
        temp_dict["TAVG"] = temp.TAVG
        temp_data.append(temp_dict)

    # return the JSON representation of dictionary
    return jsonify(temp_data)







if __name__ == "__main__":
    app.run(debug=True)