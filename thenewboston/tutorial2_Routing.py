from flask import Flask

app = Flask(__name__)

# @ signifies a decorator - way to wrap a function and modify its behavior
# we use this to map a url to a return value
@app.route('/')
def index():
		return 'This is the homepage'


# Go to localhost/tuna
@app.route('/tuna')
def tuna():
		return '<h2>Tuna is good</h2>'


# using variables
@app.route('/profile/<username>') # putting a variable in a url
								# use corner brackets
def profile(username):
		return "<h2>Hey there %s</h2>" % username
		# localhost/Bennett will return
		# "Hey there Bennett"

@app.route('/post/<int:post_id>') # string types are implicit
								# int types are not
def show_post(post_id): # function can be a different name
	return "<h2>Post id is %d</h2>" % post_id
	# hostname/post/bennett returns page not found




if __name__ == "__main__": 
		app.run(debug=True) 
