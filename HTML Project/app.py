# Importing Flask and other dependencies
import datetime as dt
import numpy as np
import pandas as pd
from config import db_password
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template
#################################################
# Flask Setup Creating flask app instance
#################################################

app = Flask(__name__)
#################################################
# Flask Routes
#################################################
#  Database
engine = create_engine(f"postgresql://postgres:{db_password}@database-1.c8vbe2aqcoj9.us-west-1.rds.amazonaws.com/datasciencesalary")
Base = automap_base()
Base.prepare(engine, reflect=True)
# Measurement = Base.classes.measurement
# Station = Base.classes.station
session = Session(engine)
print(Base.classes.keys())


#  Init Database
# db=SQLAlchemy(app)
#  Class/Model


# id = db.Column(db.Integer, primary_key=True)
# name = db.Column(db.String(100), unique=True)
# description = db.


# Updated api -------
# df = pd.read_csv("s3://final-project-data-science/dataScience_2012_2021.csv")

# Create main route
# @app.route("/occupation")
# def occupation():
#     return df.to_json()

# wwww.something/occupation/dogs

@app.route('/data')
def api():
    conn = engine.connect()
    salary_mergeddf = pd.read_sql("select distinct state from salary_2012_2021 ", conn)
    conn.close()
    return salary_mergeddf.to_html()


# End api-----------

@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/data")
def data():

    return render_template('data.html')

@app.route("/model")
def model():
    return render_template('model.html')

# @app.route("/predictor")
# def predictor():
#     return render_template('predictor.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404



if __name__ == "__main__":
        app.run(debug=True)