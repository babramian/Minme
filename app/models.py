from app import db

class Url(db.Model):
    url = db.Column(db.String(255), primary_key=True)
    url_hash = db.Column(db.String(255), unique=True)