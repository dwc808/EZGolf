from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

#player table
class Player(db.Model):
    __tablename__ = 'player'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    stored_password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"{self.name}"
    
    def __init__(self, name):
        self.name = name

    #will need to add validation, on delete cascade etc. etc.
    #need to add all relationships as you go

#round table
class Round(db.Model):
    __tablename__ = 'round'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=datetime.date)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id', ondelete="CASCADE"), nullable=False)

    player = relationship("Player", back_populates="")

    