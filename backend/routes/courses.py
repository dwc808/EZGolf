#blueprint for courses and holes

from backend import app
from ..models import Course, Hole, Round, User, Score
from flask import request, Blueprint
from sqlalchemy import select, func, and_


bp = Blueprint('courses', __name__, url_prefix='/courses')

#creates a new course and returns the course info for the addition of holes
@bp.route('/create', methods = ['POST'])
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
    
    #subquery and statement to retrieve courses/info
    subq = select(Round.course_id).where(Round.player_id == 1)
    statement = select(Course.id,Course.course_name,Course.course_location,Course.course_par).where(Course.id.in_(subq))

    courses = {}

    #fills courses played by player - name, location, par
    for row in db.session.execute(statement):
        courses[row[0]] = {"course_name": row[1],
                           "course_location": row[2],
                           "course_par": row[3]}

    #iterate over course ids to run queries for best score
    for key in courses.keys():

        #subquery and statement to retrieve personal record for each course
        subq2 = select(func.sum(Score.strokes).label('total')).\
                    join(Round, Round.id == Score.round_id).\
                    where(Round.player_id == 1, Round.course_id == key).\
                    group_by(Round.id)
        statement2 = select(func.min(subq2.c.total))
        
        #adds the personal record for each course
        courses[key]["course_pr"] = db.session.execute(statement2).scalar()

    return courses

@bp.route('/course_history', methods = ['POST'])
def course_history():
    #TODO - should this just take in ID, and load rest, or does it make sense
    # to just pass info you already have back and forth?

    #course overview
    #retrieve course id, name, location, par from front, return with records
    id = request.json['id']
    player_id = request.json['player_id']
    name = request.json['name']
    location = request.json['location']
    par = request.json['par']
    pr = request.json['pr']
   
    #retrieve hole ids, numbers
    statement = select(Hole.id, Hole.hole_number).where(Hole.course_id == id)

    holes = {}

    for row in db.session.execute(statement):
        holes[row[0]] = {"hole_number": row[1]}

    #retrieve best score for each hole, add to dict
    for key in holes.keys():
        subq = select(Score.strokes).where(and_(Score.player_id == 1, Score.hole_id == key))
        statement_2 = select(func.min(subq.c.strokes))

        holes[key]["hole_pr"] = db.session.execute(statement_2).scalar()

    #retrieve all rounds played on this course by player (date, score)
    statement_3 = select(Round.date, func.sum(Score.strokes)).join_from(Round, Score).where(and_(Round.player_id == 1, Round.course_id == id)).group_by(Round.id)

    rounds = {}

    for row in db.session.execute(statement_3):
        rounds[str(row[0])] = row[1]


    #combine rounds and holes dictionaries to return
    combined = {}
    combined["rounds"] = rounds
    combined["holes"] = holes

    return combined