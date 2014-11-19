from flask import Blueprint

auth = Blueprint('auth', __name__)

# import views and models needed here at bottom
from . import views, forms