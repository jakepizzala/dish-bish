from flask import Flask, render_template, flash, request, redirect, url_for
from datetime import datetime
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, HiddenField, SelectField
from database import Database

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'ourappissecretandcoolokay'


class ReusableForm(Form):
    name = SelectField('Name:', validators=[validators.required()])
    task = HiddenField('Task:', validators=[validators.required()])


@app.route('/', methods=['GET', 'POST'])
def homepage():
    tasks = get_tasks()
    users = get_users()
    form = ReusableForm(request.form)
    if request.method == 'POST':
        user = request.form['name']
        task = request.form['task']
        make_entry(user, task)
        # submit entry database
        return redirect(url_for('leaderboard'))
    else:
        return render_template("homepage.html", form=form, tasks=tasks, users=users)


@app.route('/leaderboard')
def leaderboard():
    counts = get_points_for_users()
    return render_template("leaderboard.html", counts=counts)


@app.route('/addtask')
def addtask():
    return render_template("addtask.html")


def get_points_for_users():
    db = Database()
    rows = db.query("SELECT u.name, COUNT(e.id) FROM events e INNER JOIN users u ON e.user_id = u.id WHERE task_id = 1 GROUP BY u.name ORDER BY COUNT(e.id) desc")
    counts = []
    for row in rows:
        counts.append({'name': row[0], 'points': row[1]})
    return counts


def get_tasks():
    db = Database()
    rows = db.query("SELECT name_external, id FROM tasks")
    tasks = []
    for row in rows:
        tasks.append({'name': row[0], 'id' : row[1]})
    return tasks


def make_entry(user, task):
    now = datetime.now()
    event = {'user_id': user, 'task_id': task, 'start_time': now}
    db = Database()
    db.insert("events", event)
    return True


def get_users():
    db = Database()
    rows = db.query("SELECT id, name FROM users ORDER BY name")
    users = []
    for row in rows:
        users.append({'id': row[0], 'name': row[1]})
    return users


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
