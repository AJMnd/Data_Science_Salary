# Importing Flask and other dependencies

from flask import Flask, render_template

#################################################
# Flask Setup Creating flask app instance
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
# @app.route("/home")
def home():
    return 'Economy in America Analysis'


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/data")
def data():
    return render_template('data.html')



if __name__ == "__main__":
        app.run(debug=True)