#!/usr/bin/env python
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import MySQLdb

db=MySQLdb.connect(passwd="3054",db="playground", user="root", host="localhost")
cursor = db.cursor(MySQLdb.cursors.DictCursor)
app = Flask(__name__)
CORS(app)
dbCreate = "INSERT INTO customers (name, count) VALUES (%s, %s)"
dbReplace = "UPDATE customers SET count = %s WHERE name = %s"
dbDelete = "DELETE FROM customers WHERE id = %s"

@app.route("/customers", methods=['GET'])
def index():
    cursor.execute('SELECT * FROM customers')
    return jsonify(cursor.fetchall())
"""
def query(table):
    with open("DataBase.json") as data_base:
        data = json.load(data_base)
    return data[table]
"""
@app.route('/customers', methods=['POST'])
def add_customer():
#    obj = adding_customer(request.json)
    obj = request.json
    cursor.execute(dbCreate, (obj['name'], obj['count']))
    cursor.execute('COMMIT')
    return (jsonify(obj))

@app.route('/customers', methods=['PUT'])
def withdrawal_money():
#    obj = calc_count(request.json)
    obj = request.json
    # print(obj)
    cursor.execute(dbReplace, (obj['count'], obj['name']))
    cursor.execute('COMMIT')
    return (jsonify(obj))
"""
def calc_count(value):
    value['customer']['count'] = int(value['customer']['count'])
    with open("DataBase.json", 'r') as data_base:
        data = json.load(data_base)
    try:
        with open("DataBase.json", 'w') as data_base:
            data['customers'][value['index']]['count'] = value['customer']['count']
            json.dump(data, data_base, indent=4)
    except Exception as e:
        print(e)
    return data

def adding_customer(value):
    value['count'] = int(value['count'])
    with open("DataBase.json", 'r') as data_base:
        data = json.load(data_base)
        data["customers"].append(value)
    try:
        with open("DataBase.json", 'w') as data_base:
            json.dump(data, data_base, indent=4)
    except Exception as e:
        print(e)
    return data
"""
@app.route('/customers', methods=['DELETE'])
def delete():
    obj = request.args
    cursor.execute(dbDelete, [obj['id']])
    cursor.execute('COMMIT')
#    obj = delete_user(int(request.args['id']))
    return (jsonify(obj))
"""
def delete_user(value):
    with open("DataBase.json", 'r') as data_base:
        data = json.load(data_base)
    try:
        with open("DataBase.json", 'w') as data_base:
            del data['customers'][value]
            json.dump(data, data_base, indent=4)
    except Exception as e:
        print(e)
    return data
"""
app.run('localhost', port=5000, debug=True)