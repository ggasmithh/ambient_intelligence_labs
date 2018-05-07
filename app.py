from flask import Flask, render_template, redirect, url_for, session, request, jsonify
import userdb

app = Flask(__name__)

@app.route('/tasks/', methods=['GET'])
@app.route('/tasks', methods=['GET'])
def tasks():
    return jsonify(userdb.show_tasks())

@app.route('/tasks/<tid>', methods=['GET'])
def task(tid):
    return jsonify(userdb.show_tasks(tid))

@app.route('/tasks/', methods=['POST'])
def insert_task():
    if request.headers['Content-Type'] == 'application/json':
        
        if "urgent" in request.json:
            userdb.insert_task(request.json["task"], request.json["urgent"])

        else:
            userdb.insert_task(request.json["task"], 0)

        
        response = jsonify(
                { 'message': "POST Successful"})

    else:
        response = jsonify(
                { 'message': "Invalid Request"})
        response.status_code = 404

    return response
    

@app.route('/tasks/<tid>', methods=['DELETE'])
def delete_task(tid):
    if userdb.delete_task(tid):
        response = jsonify(
                { 'message': "DELETE Successful"})
    
    else:
        response = jsonify(
                { 'message': "Invalid Request"})
        response.status_code = 404
    
    return response
    
if __name__ == '__main__':
    app.run()

