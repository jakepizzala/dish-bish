from flask import Flask, render_template
from database import Database
app = Flask(__name__)

@app.route('/')
def homepage():
	db = Database()
	row = db.query("SELECT id, name, name_external FROM tasks")
	data = {
		'id' : row[0][0],
		'name' : row[0][1],
		'name_external' : row[0][2]
	}
	return render_template("homepage.html", data=data)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
