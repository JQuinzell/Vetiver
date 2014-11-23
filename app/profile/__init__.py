from flask import Blueprint

profile = Blueprint('profile', __name__)

# import views and models needed here at bottom
from . import views, forms