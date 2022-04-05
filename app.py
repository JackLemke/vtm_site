
   
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/about')
def about():
    return render_template('about.html', pageTitle = 'About Page')

@app.route('/')
def base():
    return render_template('base.html', pageTitle = 'Home Page')

@app.route('/estimate')
def estimate():
    return render_template('estimate.html', pageTitle = 'Estimate Page')

@app.route('/index')
def index():
    return render_template('index.html', pageTitle = 'Index Page')     

if __name__ == '__main__':
    app.run(debug=True)