#blueprint for rounds and scores
from backend import app, db
from ..models import Round, Score, User, Course, Hole
from flask import request, Blueprint
from sqlalchemy import select, desc

bp = Blueprint('rounds', __name__, url_prefix='/rounds')

#creates a new round and returns round info to add scores
@bp.route('/new', methods = ['POST'])
def add_round():
    date = request.json['date']
    user_id = request.json['user_id']
    course_id = request.json['course_id']

    round = Round(date, user_id, course_id)
    db.session.add(round)
    db.session.commit()

    return round.format_round()

#enter score information for a round TODO note that this may need to be heavily changed later. null scores may need to be auto placed and then entering on front end will actually
# be updating the score. not sure how that will look yet - but would want to allow live entry while golfing and prevent losing already entered info if you leave the page...
@bp.route('/enter_scores', methods = ['POST']) #note, you'll probably want to tie this route to the round id, to allow returning to it?
def enter_scores():
    scores = request.json
    score_info = []

    for score in scores:
        putts = score['putts']
        shots_to_green = score['shots_to_green']
        user_id = score['user_id']
        round_id = score['round_id']
        hole_id = score['hole_id']

        add_score = Score(putts, shots_to_green, user_id, round_id, hole_id)
        db.session.add(add_score)
        db.session.commit()

        score_info.append(add_score.format_score())

    return score_info

@bp.route('/history', methods = ['GET'])
def round_history():

    #retrieve last ten rounds for user
    statement = select(Round).order_by(desc(Round.date)).limit(10)

    result = db.session.execute(statement).scalars()
    
    round_history = [row.format_round() for row in result]

    return round_history

    