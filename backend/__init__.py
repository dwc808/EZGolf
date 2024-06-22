from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
from .models import db

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:xsqu4l1xz9@localhost/EZGolf'
db.init_app(app)

@app.route('/')
def hello():
    return 'hey'

from .routes import courses
app.register_blueprint(courses.bp)

from .routes import rounds
app.register_blueprint(rounds.bp)


