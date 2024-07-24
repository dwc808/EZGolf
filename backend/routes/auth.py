from backend import app
from flask import request, Blueprint
from ..models import db, User

bp = Blueprint('auth', __name__, url_prefix='/auth')



