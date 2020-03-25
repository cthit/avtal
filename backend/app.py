from datetime import datetime, timezone
import uuid
from uuid import UUID
from flask import Flask, Response, request
from flask_restful import Resource, Api
import json
from os import listdir
from os.path import isfile, join
from flask_cors import CORS

import db
import auth
import setup

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# YYYY-MM-DDTHH:MM:SS
#
#
#
#
#


class Agreement(Resource):
    def get(self, service_name):
        path = db.get_agreement_location(service_name)
        with open(path) as file:
            return file.read()


class Accepted(Resource):
    def get(self, service_name):
        user = auth.debug_authenticate()
        try:
            last_updated = db.get_agreement_updated(service_name)
        except Exception as e:
            return 404, str(e)

        user_accepted = db.get_agreement_accepted(service_name, user)
        return user_accepted is not None and user_accepted > last_updated

    def put(self, service_name):
        user = auth.debug_authenticate()
        service = db.get_service(service_name)
        now = datetime.now(timezone.utc)
        if service is None:
            return 404, "Service not found: " + str(service_name)
        ua = db.get_agreement(service_name, user)
        if ua is None:
            try:
                db.accept_agreement(user, service_name)
                return
            except Exception as e:
                return 400, str(e)
        else:
            db.update_agreement(user, service_name)


api.add_resource(Agreement, '/api/agreement/<string:service_name>')
api.add_resource(Accepted, '/api/accept/<string:service_name>')

if __name__ == '__main__':
    setup.init_db()
    app.run()
