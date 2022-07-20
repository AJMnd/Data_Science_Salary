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
@app.route("/home")
def home():
    return render_template('home.html')


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