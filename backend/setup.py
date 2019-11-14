import json
from db import Service
import datetime
from pony.orm import db_session


@db_session
def init_db():
    with open('services.json') as json_file:
        data = json.load(json_file)
        for service in data:
            service_name = service["name"]
            agreement_location = service["location"]
            last_updated = datetime.datetime.fromisoformat(
                service["last_updated"])
            s = Service.get(service_name=service_name)
            if s is None:
                Service(service_name=service_name,
                        agreement_location=agreement_location, last_updated=last_updated)
            else:
                s.last_updated = last_updated
                s.agreement_location = agreement_location
