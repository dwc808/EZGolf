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

    #relationships
    round = db.relationship("Round", back_populates="player")
    score = db.relationship("Score", back_populates="player")

    #will need to add validation etc.
    

#round table
class Round(db.Model):
    __tablename__ = 'round'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=datetime.date)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id', ondelete="CASCADE"), nullable=False)

    player = db.relationship("Player", back_populates="round")
    course = db.relationship("Course", back_populates="round")
    score = db.relationship("Score", back_populates="round")

    #will need to add validation etc.

#course table
class Course(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(45), nullable=False, unique=True)  #maybe get rid of unique later and let each user make their own courses
    course_location = db.Column(db.String(45), nullable=False)  #town? should you have town and state?
    round_id = db.Column(db.Integer, db.ForeignKey('round.id', ondelete="CASCADE"), nullable=False)

    round = db.relationship("Round", back_populates="course")
    hole = db.relationship("Hole", back_populates="course")
    
    #will need to add validation etc.

#hole table
class Hole(db.Model):
    __tablename__ = 'hole'

    id = db.Column(db.Integer, primary_key=True)
    hole_number = db.Column(db.Integer, nullable=False)
    par = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id', ondelete="CASCADE"), nullable=False)

    course = db.relationship("Course", back_populates="hole")
    score = db.relationship("Score", back_populates="hole")

    #will need to add validation etc.

#score table
class Score(db.Model):
    __tablename__ = "score"

    id = db.Column(db.Integer, primary_key=True)
    putts = db.Column(db.Integer, nullable=False)
    shots_to_green = db.Column(db.Integer, nullable=False)
    strokes = db.Column(db.Integer, nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id', ondelete="CASCADE"), nullable=False)
    round_id = db.Column(db.Integer, db.ForeignKey('round.id', ondelete="CASCADE"), nullable=False)
    hole_id = db.Column(db.Integer, db.ForeignKey('hole.id', ondelete="CASCADE"), nullable=False)

    player = db.relationship("Player", back_populates="score")
    round = db.relationship("Round", back_populates="score")
    hole = db.relationship("Hole", back_populates="score")

    #will need to add validation etc.


    