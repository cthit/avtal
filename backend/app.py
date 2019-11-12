import datetime
import uuid
from uuid import UUID
from flask import Flask, Response, request
import json
from os import listdir
from os.path import isfile, join

import db
import auth

app = Flask(__name__)

# YYYY-MM-DDTHH:MM:SS

last_updated = {
    "hubbit": datetime.datetime.fromisoformat("2019-10-18T20:10:25"),
    "bookit": datetime.datetime.fromisoformat("2019-08-18T20:10:25")
}


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/agreements', methods=['GET'])
def get_all_agreements():
    user_id = request.args.get('user_id')
    user_agreement = db.get_agreement(user_id)

    agreement_path = "./agreements/"
    files = [f for f in listdir(agreement_path)
             if isfile(join(agreement_path, f))]
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


@app.route('/api/me', methods=['GET'])
def get_me():
    return db.get_agreement()


@app.route('/api/fun', methods=['POST'])
def set_data():
    req_data = request.get_json()
    hubbit = datetime.datetime.fromisoformat(req_data['hubbit'])
    bookit = datetime.datetime.fromisoformat(req_data['bookit'])
    db.set_agreement(hubbit, bookit)
    return ""


@app.route('/api/accept')
def accept():
    logged_in_id = auth.debug_authenticate()
    req_data = request.args.get('service')
    agreement = db.get_agreement(logged_in_id)
    set_time_now(agreement.get_column_by_string(req_data))


def set_time_now(service):
    service = datetime.datetime.now()


if __name__ == '__main__':
    app.run()

# Supply and store markdown files.
