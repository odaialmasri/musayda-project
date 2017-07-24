from flask import Flask,render_template, request
import dataset


app = Flask(__name__)





@app.route("/")
def home_page():
	return render_template("index.html")


@app.route("/form")
def form_date():
	return render_template("form.html")


@app.route("/form_posts",methods=["POST"])
def form_res():
	user_firstname = request.form["firstname"]
	user_lastname = request.form["lastname"]
	user_message = request.form["message"]
	user_gender = request.form["gender"]






if __name__ == "__main__":
	app.run()