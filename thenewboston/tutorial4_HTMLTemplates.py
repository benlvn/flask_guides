from flask import Flask, render_template
# importing this allows us to use html templating


# dir templates --- for html templates
# dir static --- all of the static, nonchanging files (css)
# These are default directory name, flask looks for them
app = Flask(__name__)

@app.route("/profile/<name_in>")
def profile(name_in):
		# Never put html directly in your return message
		# like don't do this -----> return "Homepage"
		return render_template("tut4_profile.html", name=name_in)
		# We're passing in a variable called name
		# The html template can use it be typing {{ name }}





if __name__ == "__main__":
		app.run()
