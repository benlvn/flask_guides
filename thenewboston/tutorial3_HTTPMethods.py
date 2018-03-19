from flask import Flask, request
# request moduel gives you info on user requests

app = Flask(__name__)


@app.route('/')
def index():
		return "Method used: %s" % request.method


@app.route("/bacon", methods=['GET', 'POST'])
# The bacon page can now handle both GET and POST requests
def bacon():
	if request.method == 'POST':
			return "You are using POST" # Tested using Postman app
	else:
			return "You are probably using GET"





if __name__ == "__main__":
		app.run()
