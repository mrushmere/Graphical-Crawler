"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, url_for
from GraphicalCrawler import app
from forms import CrawlerForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def home():
    form = CrawlerForm()
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        form=form,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
