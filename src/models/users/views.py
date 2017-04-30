# views is the end point of the api related to the users

from flask import Blueprint, request, session, url_for, render_template
from werkzeug.utils import redirect
from src.models.users.user import User

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        # need user entered email and password for check
        email = request.form['email']
        password = request.form['hashed']
        #check if login is valid and if so create session
        if User.is_login_valid(email, password):
            # rememeber session is a temp storage. it has a unique id provided by us, so we know the session is associate with that email
            session['email'] = email
            # show user pages
            return redirect(url_for(".user_alerts"))
    # this is outside of the if to handle if there is GET request, show the user login
    return render_template("users/login.html")

@user_blueprint.route('/register')
def register_user():
    pass

@user_blueprint.route('/alerts')
def user_alerts():
    return "This is the alerts page"

@user_blueprint.route('logout')
def logout_user():
    pass

@user_blueprint.route('/check_alerts/<string:user_id>')
def check_user_alerts(user_id):
    pass