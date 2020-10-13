# Import flask
From flask import Flask

# Create an app
app = Flask(__name__)

# Create routes
@app.route("/")
    print("")
    return("Sqlalchemy-Challenge")
    return("Available routes")

@app.route("/api/v1.0/precipitation")
    print("")
    return("Precipitation")

@app.route("/api/v1.0/stations")
    print("")
    return("Stations")

@app.route("/api/v1.0/tobs")
    print("")
    return("tobs")

@app.route("/api/v1.0/<start>")
    print("")
    return("")

@app.route("/api/v1.0/<start>/<end>")
    print("")
    return("")

if __name__ == "__main__":
    app.run(debug=True)
