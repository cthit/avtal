import datetime
from uuid import UUID

from pony.orm import Database, Required

import config

db = Database()

class Agreement(db.Entity):
    id = Required(UUID, auto=True)
    hubbit = Required(datetime)
    bookit = Required(datetime)

db.bind(
    provider='postgres',
    user=config.POSTGRES_USER,
    password=config.POSTGRES_PASSWORD,
    host=config.POSTGRES_HOST,
    database=config.POSTGRES_DB
)

db.generate_mapping(create_tables=True)