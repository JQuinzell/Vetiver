from flask import Blueprint

main = Blueprint('main', __name__)

# import views and models needed here at bottom
from . import views, forms