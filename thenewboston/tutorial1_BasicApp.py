# Install flask
# pip install flask

from flask import Flask

app = Flask(__name__)

# routing/mapping - connecting a page to a python object
# mapped to homepage now
# could map it to like '/profile' or '/user/account'

# When the user goes to '/' flask runs and returns index()
@app.route('/')
def index():
		return 'This is the homepage'

if __name__ == "__main__": # We only run the app when this file
							# is called directly
							# otherwise we can import it into
							# another file
		app.run(debug=True) # Debug because dev mode
		# This basically says "start this app"

# Run the file and go to url 127.0.0.1:5000 (port 5000)
