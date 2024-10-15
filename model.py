from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    air_date = db.Column(db.Date, nullable=False)
    
    
    appearances = db.relationship('Appearance', backref='episode', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'air_date': self.air_date.isoformat(),
        }


class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    profession = db.Column(db.String, nullable=False)
    
    
    
    appearances = db.relationship('Appearance', backref='guest', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'profession': self.profession,
        }


class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Float, nullable=False)
    
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'episode_id': self.episode_id,
            'guest_id': self.guest_id,
        }
