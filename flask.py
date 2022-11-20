from urllib import request
from flask import Flask, jsonify, request
app = Flask(__name__)

List = [
    {
        'id': 1,
        'name': u'Raju',
        'contact': u'9987644456',
        'done': False
    },
    {
        'id': 2,
        'name': u'Rahul',
        'contact': u'9876543222',
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data"
        }, 400)
    contact = {
        'id': List[-1]['id']+1,
        'name': request.json['name'],
        'contact': request.json.get('contact', ""),
        'done': False
    }
    List.append(contact)
    return jsonify({
        'status': "Success",
        'message': "Contact added successfully"
    })
    
@app.route("/get-data")
def get_contact():
    return jsonify({
        "data": List
    })
if (__name__ == "__main__"):
    app.run(debug = True)