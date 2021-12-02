from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/about',strict_slashes=False)
def about():
	return render_template("about.html")


