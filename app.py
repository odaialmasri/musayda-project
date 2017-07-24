from flask import Flask,render_template, request
import dataset


app = Flask(__name__)





@app.route("/")
def home_page():
	return render_template("index.html")


@app.route("/form")
def form_date():
	return render_template("form.html")









if __name__ == "__main__":
	app.run()