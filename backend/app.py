import datetime
from datetime

from flask import Flask, Response, request
import json
from os import listdir
from os.path import isfile, join

import db

app = Flask(__name__)

# YYYY-MM-DDTHH:MM:SS

last_updated = {
    "hubbit" : datetime.datetime.fromisoformat("2019-10-18T20:10:25"),
    "bookit" : datetime.datetime.fromisoformat("2019-08-18T20:10:25")
}


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/agreements', methods=['GET'])
def get_all_agreements():
    agreement_path = "./agreements/"
    files = [f for f in listdir(agreement_path) if isfile(join(agreement_path, f))]
    json_objects = []
    for file in files:
        s = open(agreement_path + file, 'r')
        name = file.split('.')[0]
        x = {
            "name": name,
            "agreement": s.read(),
            "accepted": True
        }
        json_objects.append(x)

    return Response(json.dumps(json_objects), mimetype='application/json')

@app.route('/api/me', method=['GET'])
def get_me():
    pass

@app.route('/api/fun', methods=['POST'])
def set_data():
    req_data = request.get_json()
    user_id = req_data['user']
    hubbit = req_data['hubbit']
    bookit = req_data['bookit']
    db.Agreement()

if __name__ == '__main__':
    app.run()

# Supply and store markdown files.
