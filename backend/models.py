from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from backend import app, db


#user table
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    stored_password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"{self.fname}"
    
    def __init__(self, fname):
        self.fname = fname

    #relationships
    round = db.relationship("Round", back_populates="user")
    score = db.relationship("Score", back_populates="user")
    

#round table
class Round(db.Model):
    __tablename__ = 'round'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=datetime.date)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id', ondelete="CASCADE"), nullable=False)

    def __init__(self, date, user_id, course_id):
        self.date = date
        self.user_id = user_id
        self.course_id = course_id

    user = db.relationship("user", back_populates="round")
    course = db.relationship("Course", back_populates="round")
    score = db.relationship("Score", back_populates="round")

    def format_round(self):
        return {
            "date": self.date,
            "user_id": self.user_id,
            "course_id": self.course_id
        }

    # TODO will need to add validation etc.

#course table
class Course(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(45), nullable=False, unique=True)  #maybe get rid of unique later and let each user make their own courses
    course_location = db.Column(db.String(45), nullable=False)  #town? should you have town and state?
    course_holes = db.Column(db.Integer, nullable=False)
    course_par = db.Column(db.Integer, nullable=False)

    hole = db.relationship("Hole", back_populates="course")
    round = db.relationship("Round", back_populates="course")
    
    # TODO will need to add validation etc.

    def __init__(self, name, location, holes, par):
        self.course_name = name
        self.course_location = location
        self.course_holes = holes
        self.course_par = par

    #format course
    def format_course(self):
        return {
            "id": self.id,
            "course_name": self.course_name,
            "course_location": self.course_location,
            "course_holes": self.course_holes,
            "course_par": self.course_par
        }

#hole table
class Hole(db.Model):
    __tablename__ = 'hole'

    id = db.Column(db.Integer, primary_key=True)
    hole_number = db.Column(db.Integer, nullable=False)
    par = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id', ondelete="CASCADE"), nullable=False)

    def __init__(self, hole_number, par, length, course_id):
        self.hole_number = hole_number
        self.par = par
        self.length = length
        self.course_id = course_id

    course = db.relationship("Course", back_populates="hole")
    score = db.relationship("Score", back_populates="hole")

    #format hole
    def format_hole(self):
        return {
            "id": self.id,
            "hole_number": self.hole_number,
            "par": self.par,
            "length": self.length, 
            "course_id": self.course_id
        }

    # TODO will need to add validation etc.

#score table
class Score(db.Model):
    __tablename__ = "score"

    id = db.Column(db.Integer, primary_key=True)
    putts = db.Column(db.Integer, nullable=False)
    shots_to_green = db.Column(db.Integer, nullable=False)
    strokes = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    round_id = db.Column(db.Integer, db.ForeignKey('round.id', ondelete="CASCADE"), nullable=False)
    hole_id = db.Column(db.Integer, db.ForeignKey('hole.id', ondelete="CASCADE"), nullable=False)

    def __init__(self, putts, shots_to_green, user_id, round_id, hole_id):
        self.putts = putts
        self.shots_to_green = shots_to_green
        self.strokes = putts+shots_to_green
        self.user_id = user_id
        self.round_id = round_id
        self.hole_id = hole_id

    user = db.relationship("User", back_populates="score")
    round = db.relationship("Round", back_populates="score")
    hole = db.relationship("Hole", back_populates="score")

    def format_score(self):
        return {
            "id": self.id,
            "putts": self.putts,
            "shots_to_green": self.shots_to_green, 
            "strokes": self.strokes,
            "user_id": self.user_id,
            "round_id": self.round_id,
            "hole_id": self.hole_id
        }
    
    # TODO will need to add validation etc.
