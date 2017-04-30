#the project is first time for me to us a run.py, this used to be in the app.py,
#however the app should just have the app and run handle the run

from src.app import app

app.run(debug=app.config['DEBUG'], port=4990)
