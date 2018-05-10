from database import Database
from datetime import datetime

#instantiate a db
db = Database();

#Query db
email = 'jake@kiva.org'
query = "SELECT id, name, email from users where email = '" + email + "'"
user_data = db.query(query)
print(user_data)

#insert row
dt = datetime.now()
data = {
	'user_id' : user_data[0][0],
	'start_time' : str(dt),
	'task_id' : 1
}
db.insert('events', data);
