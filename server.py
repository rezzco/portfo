from flask import Flask, render_template, request, redirect
from SaveContacts import CsvWriter, Database_sql
app = Flask(__name__)


@app.route('/')
def home_rout():
    return render_template("index.html")


@app.route('/<string:page_name>')
def general_rout(page_name):
	try:
		return render_template(page_name+".html")
	except:
		return render_template("404.html")

def write_to_text_file(data):
	with open ("database.txt", mode="a") as db:
			db.write("****new entry*****\n\n")
			for k,v in data.items():
				db.write(k +": " +v+"\n")
			db.write("*************\n\n")

def write_to_csv_file(data):
	csv = CsvWriter()
	csv.dict_writer(data, method="a")

def write_to_main_db(data):
	db = Database_sql()
	db.write_to_aqllit(data)




@app.route("/submit_form", methods = ["POST", "GET"])
def submit_form():
	if request.method =="POST":
		data = request.form.to_dict()
		write_to_text_file(data)
		write_to_csv_file(data)
		write_to_main_db(data)
		
		return redirect("/thankyou")

