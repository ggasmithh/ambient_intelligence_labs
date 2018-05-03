from flask import Flask, render_template, redirect, url_for, session, request
from flask_bootstrap import Bootstrap
import userdb

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template('index.html', tasks = userdb.show_tasks())

@app.route('/delete_task/<tid>')
def delete_task(tid):
    userdb.delete_task(tid)
    return redirect(url_for('index'))

@app.route('/insert_task/', methods=['POST'])
def insert_task():
    task_desc = request.form['task_desc']
    userdb.insert_task(task_desc)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
