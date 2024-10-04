from . import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    budget = db.Column(db.Float)
    homepage = db.Column(db.Text)
    original_language = db.Column(db.String)
    overview = db.Column(db.Text)
    release_date = db.Column(db.Date, nullable=True)
    revenue = db.Column(db.Float)
    runtime = db.Column(db.Integer)
    status = db.Column(db.String)
    title = db.Column(db.String, nullable=False)
    vote_average = db.Column(db.Float)
    vote_count = db.Column(db.Integer)
    production_company_id = db.Column(db.Integer)
    genre_id = db.Column(db.Integer)
    languages = db.Column(db.String) 
