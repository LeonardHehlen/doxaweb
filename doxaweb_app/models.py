from doxaweb_app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    short_description = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.String(1000), unique=False, nullable=False)
    link = db.Column(db.String(100), unique=False, nullable=False)
    img = db.Column(db.String(100), unique=False, nullable=False)