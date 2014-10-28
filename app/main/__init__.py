from flask import Blueprint

main = Blueprint('main', __name__)

# import views

# views also import this.. How is this not circular/bad?