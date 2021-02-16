from flask import Flask, jsonify, request, redirect
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.json_util import dumps, loads
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://divjot:divjot1234@cluster0.gpz0h.mongodb.net/div?ssl=true&ssl_cert_reqs=CERT_NONE"
CORS(app)

mongo = PyMongo(app)
db_operations = mongo.db.div


@app.route('/api/getCounter')
def get_counters():
    cursor = db_operations.find({}, {"_id": 0})
    list_cur = list(cursor)
    print(list_cur)
    json_data = dumps(list_cur, indent=2)
    return json_data


@app.route('/api/updateCounter', methods=['POST'])
def update_counter():
    input_data = request.get_json()
    # print(request)
    # print('###########')
    # print("input_data", input_data)
    count = int(input_data['counter'])
    # print("******", count, "*******")
    update_query = {"name": input_data["name"]}
    new_values = {"$set": {"count": input_data["counter"]}}

    db_operations.update_one(update_query, new_values)
    return dumps(list(db_operations.find({}, {"_id": 0})))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
