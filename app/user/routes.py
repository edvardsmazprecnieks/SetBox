from flask import Blueprint, render_template, redirect, url_for, request
from app import app

blueprint = Blueprint('user', __name__)

@blueprint.route('/')
def index():
    return render_template('user/index.html')

@blueprint.route('/login')
def login():
    return render_template('user/login.html')

@blueprint.route('/register')
def register():
    return render_template('user/registration.html')

