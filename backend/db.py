import datetime
import json
import uuid
from uuid import UUID

from flask import Response
from pony.orm import Database, Required, db_session, PrimaryKey, commit

import config

db = Database()


class Agreement(db.Entity):
    id = PrimaryKey(UUID, auto=False)
    hubbit = Required(datetime.datetime)
    bookit = Required(datetime.datetime)

    def get_column_by_string(self, name):
        x = {
            "hubbit": self.hubbit,
            "bookit": self.bookit
        }
        return x[name]


@db_session
def get_agreement(id):
    a = Agreement.get(id=id)
    if a is None:
        a = Agreement(id=id)
        print("ahsdhasdhahsd")
        commit()
    return a


@db_session
def set_agreement(hubbit, bookit):
    agreement = Agreement(hubbit=hubbit, bookit=bookit)
    commit()


db.bind(
    provider='postgres',
    user=config.POSTGRES_USER,
    password=config.POSTGRES_PASSWORD,
    host=config.POSTGRES_HOST,
    database=config.POSTGRES_DB
)

db.generate_mapping(create_tables=True)
