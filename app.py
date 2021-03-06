import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask import Flask, render_template, redirect, request, url_for
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = os.environ.get('Mongo')


mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template('tasks.html', tasks=mongo.db.Tasks.find())


@app.route('/add_task')
def add_task():
    return render_template('addtask.html',
                           categories=mongo.db.Categories.find())


@app.route('/insert_task', methods=['POST'])
def insert_task():
    tasks = mongo.db.Tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
