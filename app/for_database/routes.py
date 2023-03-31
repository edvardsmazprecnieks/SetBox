from flask import Blueprint, render_template
from app import app
from app.extensions.database.crud import recreate_database

blueprint = Blueprint('for_database', __name__)

@blueprint.route('/temp_recreate_database')
def recr_database():
    recreate_database()
    return "<p>Done!</p>"