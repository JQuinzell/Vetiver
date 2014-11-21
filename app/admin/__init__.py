from flask import Blueprint

admin = Blueprint('admin', __name__)

# import views and models needed here at bottom
from . import views, forms