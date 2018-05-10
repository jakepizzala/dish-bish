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
    db = Database()
    row = db.query("SELECT id, name, name_external FROM tasks")
    data = {
        'id': row[0][0],
        'name': row[0][1],
        'name_external': row[0][2]
    }
    form = ReusableForm(request.form)
    if request.method == 'POST':
        name = request.form['name']
        task = request.form['task']
        # submit entry database
        return redirect(url_for('leaderboard'))
    else:
        return render_template("homepage.html", form=form, data=data)


@app.route('/leaderboard')
def leaderboard():
    counts = [
        {'name': 'Jake', 'points': 10},
        {'name': 'Elli', 'points': 12},
        {'name': 'Colleen', 'points': 5},
        {'name': 'David', 'points': 15}
    ]
    new_counts = sorted(counts, key=lambda k: k['points'], reverse=True)
    return render_template("leaderboard.html", counts=new_counts)


@app.route('/addtask')
def addtask():
    return render_template("addtask.html")


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
