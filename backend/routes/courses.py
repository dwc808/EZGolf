#blueprint for courses and holes

from backend import app
from ..models import db, Course, Hole
from flask import request, Blueprint

bp = Blueprint('courses', __name__, url_prefix='/courses')

#creates a new course and returns the course info for the addition of holes
@bp.route('/create', methods = ['POST'])
#create a new course
def create_course():
    course_name = request.json['course_name']
    course_location = request.json['course_location']
    course_holes = request.json['course_holes']
    course_par = request.json['course_par']

    course = Course(course_name, course_location, course_holes, course_par)
    db.session.add(course)
    db.session.commit()

    return course.format_course()

#takes in info for the holes associated with the course
@bp.route('/holes', methods = ['POST'])

def add_holes():

    holes = request.json
    hole_info = []

    for hole in holes:
        hole_number = hole['hole_number']
        par = hole['par']
        length = hole['length']
        course_id = hole['course_id']

        add_hole = Hole(hole_number, par, length, course_id)
        db.session.add(add_hole)
        db.session.commit()
        hole_info.append(add_hole.format_hole())

    #TODO temporary return - may need to return info for all holes to verify correct input on frontend
    return hole_info

#takes in player_id and returns all courses played with par, location, and personal best score
@bp.route('/player', methods = ['GET'])     #player id should be the route here

def player_courses():
    pass