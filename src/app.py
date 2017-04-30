#get price of item in a web-store for a user under a price limit

# User creates an alert, Gives us an email, gives us a price and item URL
# We check the price, if price is < limit, notify the user via email, repeat every x time
# Models:
    # Alerts = email, price limit, item created  with url
    # item = Name, Price, Url
    # Website = How to check item's price
    # Users = e-mail for notification, name/password/username

from flask import Flask, render_template
from src.common.database import Database

app = Flask(__name__)
app.config.from_object('src.config')
#secure session. when browser request page for the app, Flask gives the browser a cookie with a session id
#session id links that browser to a specific session on our server
#session on our server contains things like the email to verify if user is logged in our not
#secret_key used to secure the cookies we provide to the browser
app.secret_key = "123" #normally you should use 32 letters and numbers

@app.before_first_request
def init_db():
    Database.initialize()

from src.models.users.views import user_blueprint
app.register_blueprint(user_blueprint, url_prefix="/users")


