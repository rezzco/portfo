import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def connect_to_db():
	return create_connection("contact_db.sqlite")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")



def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_query(email, subject, message):
	Insert_contact =  f"INSERT INTO contacts (email, subject, message) VALUES ('{email}', '{subject}', '{message}');"
	return Insert_contact
def read_query():
	return "SELECT * from contacts"



if __name__ =="__main__":
	connection = create_connection("contact_db.sqlite")
	create_contacts_table = """
	CREATE TABLE IF NOT EXISTS contacts (
	  id INTEGER PRIMARY KEY AUTOINCREMENT,
	  email TEXT NOT NULL,
	  subject TEXT,
	  message TEXT
	);
	"""
	execute_query(connection, create_contacts_table)
# 	Insert_contact =  """
# INSERT INTO
#   contacts (email, subject, message)
# VALUES
#   ('test@test.com', 'test', 'test1'),
#   ('test@test.com', 'test', 'test2');
# """
# 	execute_query(connection, Insert_contact)
	select_contacts = "SELECT * from contacts"
	contacts = execute_read_query(connection, select_contacts)

	for contact in contacts:
	    print(contact)