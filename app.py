from flask import Flask, render_template, redirect, url_for, session, request, jsonify
import userdb

app = Flask(__name__)

@app.route('/tasks/', methods=['GET'])
def tasks():
    return jsonify(userdb.show_tasks())

@app.route('/tasks/<tid>', methods=['GET'])
def task(tid):
    return jsonify(userdb.show_tasks(tid))

if __name__ == '__main__':
    app.run()

