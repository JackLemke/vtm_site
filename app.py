import app
from flask import Flask
from flask import render_template, request, url_for

app = Flask(__name__)

@app.route('/about')
def about():
    return render_template('about.html', pageTitle = 'About Page')

@app.route('/')
def base():
    return render_template('base.html', pageTitle = 'Home Page')

@app.route('/estimate', methods=['GET','POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = float(form['radius'])
        height = float(form['height'])
        pi = 3.14
        top_tank = pi * radius**2
        side_tank = 2 * (pi * (radius*height)) * 2
        area_tank = top_tank + side_tank
        sqft = area_tank / 144
        cost_material = 25 * sqft
        cost_labor = 15 * sqft
        estimate_total = "${:,.2f}".format(round(cost_labor + cost_material, 2))
        return render_template('estimate.html', estimate = estimate_total)
    return render_template('estimate.html', pageTitle= 'Vertical Tank Maintenance Estimator')

@app.route('/index')
def index():
    return render_template('index.html', pageTitle = 'Index Page')     

if __name__ == '__main__':
    app.run(debug=True)
