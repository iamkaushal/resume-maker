# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template



app = Flask(__name__)

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/resume')
def resume():
    try:
        return render_template('resume.html')
    except Exception as e:
        return str(e)


@app.route('/about')
def about():
    try:
        return render_template('about.html')
    except Exception as e:
        return str(e)


@app.route('/contact')
def contact():
    try:
        return render_template('contact.html')
    except Exception as e:
        return str(e)


# @app.route('/')
# def index():
#     abort(404) #returns 404 error
#     render_template('index.html') #this never gets executed


if __name__ == '__main__':
    app.run(debug=True)
