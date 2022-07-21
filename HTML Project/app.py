# Importing Flask and other dependencies

from flask import Flask, render_template

#################################################
# Flask Setup Creating flask app instance
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# engine = create_engine("database-1.c8vbe2aqcoj9.us-west-1.rds.amazonaws.com")

# need password, port, and username
# `postgresql://user_name:password@aws_url/database_name`
# Base = automap_base()
# Base.prepare(engine, reflect=True)
# Measurement = Base.classes.measurement
# Station = Base.classes.station
# session = Session(engine)

# Updated api -------
df = pd.read_csv("s3://final-project-data-science/dataScience_2012_2021.csv")

# Create main route
# @app.route("/occupation")
# def occupation():
#     return df.to_json()

# User wants to filter data
@app.route('/occupation/<name>')
def api(name):
    return df.query("occupation == {name}").to_json()

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

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
        app.run(debug=True)