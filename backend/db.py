from datetime import datetime, timezone
import json
import uuid
from uuid import UUID

from flask import Response
from pony.orm import Database, Required, db_session, PrimaryKey, commit

import config
from pony.orm.core import Set
from pony import orm

db = Database()


class Service(db.Entity):
    service_name = PrimaryKey(str)
    agreement_location = Required(str)
    last_updated = Required(datetime)
    user_agreeds = Set("UserAgreed")


class UserAgreed(db.Entity):
    user_id = Required(UUID)
    service = Required(Service)
    accepted_date = Required(datetime)
    PrimaryKey(user_id, service)


@db_session
def get_agreement_location(service: str):
    s = Service.get(service_name=service)
    if s is not None:
        return s.agreement_location
    raise Exception("Service not found: " + str(service))


@db_session
def get_agreement_updated(service: str):
    s = Service.get(service_name=service)
    if s is not None:
        return s.last_updated
    raise Exception("Service not found: " + str(service))


@db_session
def get_agreement_accepted(service: str, user: UUID):
    ua = orm.select(agreement for agreement in UserAgreed
                    if agreement.user_id == user and
                    agreement.service.service_name == service).first()
    if ua is not None:
        return ua.accepted_date
    return None


@db_session
def get_service(service: str):
    return Service.get(service_name=service)


@db_session
def get_agreement(service: str, user: UUID):
    return UserAgreed.select(lambda ua: ua.user_id == user and
                             ua.service.service_name == service).first()


@db_session
def accept_agreement(user: UUID, service: str):
    now = datetime.now(timezone.utc)
    UserAgreed(user_id=user, service=service, accepted_date=now)


@db_session
def update_agreement(user: UUID, service: str):
    ua = get_agreement(service, user)
    ua.accepted_date = datetime.now(timezone.utc)


db.bind(
    provider='postgres',
    user=config.POSTGRES_USER,
    password=config.POSTGRES_PASSWORD,
    host=config.POSTGRES_HOST,
    database=config.POSTGRES_DB
)

db.generate_mapping(create_tables=True)
