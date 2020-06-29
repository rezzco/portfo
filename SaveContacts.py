import csv
import shit as db



class Database_sql():
	def __init__(self,):
		pass

	def write_to_aqllit(self, data):
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		cn = db.connect_to_db()
		insert_query = db.insert_query(email, subject, message)
		db.execute_query(cn, insert_query)
		show_db = db.read_query()
		results = db.execute_read_query(cn, show_db)
		for row in results:
			print(row)








class CsvWriter():
	def dict_writer(self, dict_data, method):
		row=[]
		for k,v in dict_data.items():
			row.append(v)
		with open("database.csv" , mode=method , newline="") as db:
			db_writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			db_writer.writerow(row)


