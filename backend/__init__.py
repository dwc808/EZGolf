from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, session
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'e03499e85d1c2aaa30453d88767a3d87d81b062ae6a359e8edd20131e1a44e25'
CORS(app)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:xsqu4l1xz9@localhost/EZGolf'
db.init_app(app)
migrate = Migrate(app, db)

from .routes import courses
app.register_blueprint(courses.bp)

from .routes import rounds
app.register_blueprint(rounds.bp)


