from flask import Flask, request, Response, jsonify
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

def get_client():
    client = MongoClient('10.129.5.104',port=27017,username='adminuser', password='adminpass1234', authSource="records_db")
    return client




client=get_client()
#db = client["records_db"]
#_records = db.records_tb.find()
#records = [{"type": record["type"], "network": record["network"]} for record in _records]


records = []

@app.route('/')          #the main index entry point to our app 

def main():
    return "hello"



@app.route('/records', methods=['GET'])  
def get_records():

    try:
        log = client.admin.command('ping')
    except:
        log = 'Server not available'
    return log


@app.route('/records', methods=['POST'])
def add_records():
    data = request.get_json(force=True)
    record = {
        'type': data['type'],
        "network" : data["network"]
    }
    db.records_tb.insert_one(record)

    return jsonify(
        status=True,
        message='record saved successfully!'
    ), 201



if __name__ == "__main__":
    app.run(host="0.0.0.0", port='8080')
