from flask import Flask,render_template, request
import dataset


app = Flask(__name__)

# db=dataset.connect("postgres://yowahpfaxtsjoc:89e78de430594fa7bffec234ce5bc8ac9193cef0a864378fd900ddd573d65651@ec2-23-23-244-83.compute-1.amazonaws.com:5432/dbn2rcviq5s3i4")

# table=db["musa3ada_users"]




@app.route("/")
def home_page():
	return render_template("index.html")


@app.route("/form")
def form_date():
	return render_template("form.html")



@app.route("/charitries")
def charitries_page():
	return render_template("charitries.html")




@app.route("/form_posts",methods=["POST"])
def form_posts():
	user_name = request.form["name"]
	user_email= request.form["Email"]
	user_phonenumber = request.form["phone_number"]
	user_status = request.form["msg"]

	# user1 = table.insert(dict(username=user_name,Email=user_email,phonenumber=user_phonenumber,user_info=user_status))

	# user2= table.find()

	# user_list=list(user2)

	


@app.route("/display_stories")
def display():
	return render_template("view.html")

if __name__ == "__main__":
	app.run(port=5555)