from app import app, db
from app.models import *
from flask import render_template, request, redirect
from Base_62_Converter import encode62
import re

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_url', methods=('GET', 'POST'))
def create_url():
    u = None
    if request.method == 'POST':
        url = request.form['url']

        if url.startswith('http'):
            url = re.sub(r'https?:\\', '', url)
        if url.startswith('www.'):
            url = re.sub(r'www.', '', url)

        if '.' not in url:
            return "Error: Not a URL"

        u = Url.query.filter_by(url=url).first()

        if not u:
            u = Url(url=url, url_hash=encode62(db.session.query(Url).count()).zfill(6))
            db.session.add(u)
            db.session.commit()

    if not u:
        return render_template('index.html')


    return render_template('index.html', shortened_url = f'Shortened URL: http://min.me/{u.url_hash}',
                            original_url=f'Original URL: {u.url}')

@app.route('/<hash>')
def find_url(hash):
    u = Url.query.filter_by(url_hash=hash).first()
    if not u:
        return 'Error: URL does not exist'

    return redirect(f'http://{u.url}')
