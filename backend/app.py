from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:xsqu4l1xz9@localhost/EZGolf'
from models import db
db.init_app(app)

@app.route('/')
def hello():
    return 'hey'

if __name__ == '__main__':
    app.run()
