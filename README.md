# sqlalchemy-challenge
Michael Bien sqlalchemy challenge homework

The homework was comprised of two parts:

1. Bien_climate_starter: Jupyter notebook of climate analysis
    Explored the hawaii.sqlite data
    
    One Year of Precipitation Analysis:
    a. Isolated one year of precipitation data and converted to dataframe
    b. Plotted the one year precipitation using df.plt
    c. Calcuated the summary statistics using df.describe()

    Stations Analysis:
    a. Analysed maesurement data and returned dictionary of stations with row counts in descending order
    b. Calcuated the lowest, highest and average temperatures for the most active station USC00519281 with 2772 obserations
    c. Determined the number of tobs for the station from b. USC00519281 with 352 tobs
    d. Created histogram of tobs for station USC00519281

2. Flask app - created a flask app with multiple routes:
    a. Precipitation: /api/v1.0/precipitation > returns one year of precipitation data
    b. Stations: /api/v1.0/stations > returns a JSON of stations and the count of measurements in descending order
    c. Tobs: /api/v1.0/tobs > returns one years of temperature observations (tobs) for station USC00519281
    d. Start Date End Date: /api/v1.0/start_date/end_date > return the minimum, maximum and average temperatures when:
        1. A start date is entered in the format of YYYY-MM-DD
        or
        2. A start date and end date are entered in the format of YYYY-MM-DD





