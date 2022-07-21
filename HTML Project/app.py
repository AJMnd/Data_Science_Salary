# Importing Flask and other dependencies
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#################################################
# Flask Setup Creating flask app instance
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

#  Database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://user_name:password@database-1.c8vbe2aqcoj9.us-west-1.rds.amazonaws.com'
#  Init Database
db=SQLAlchemy(app)
#  Class/Model
class results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.

# Updated api -------
# df = pd.read_csv("s3://final-project-data-science/dataScience_2012_2021.csv")

# Create main route
# @app.route("/occupation")
# def occupation():
#     return df.to_json()

# User wants to filter data
# @app.route('/occupation/<wage>')
# def api(wage):
#     return df.query("occupation == {wage}").to_json()


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