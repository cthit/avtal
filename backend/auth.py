from flask import request
from rauth import OAuth2Service
import requests
import config
from uuid import UUID


def authenticate():
    gamma = OAuth2Service(
        config.FRONTEND_CLIENT_ID,
        config.FRONTEND_CLIENT_SECRET,
        'gamma',
        config.FRONTEND_REDIRECT_URI
    )
    session = gamma.get_auth_session()
    user = session.get('me').json()
    return user['id']


def debug_authenticate():
    return UUID('{12345678-1234-5678-1234-567812345678}')


def auth_required(f):
    auth = request.headers.get('Authorization')
    if auth:
        r = requests.get("http://localhost:8081/api/users/me",
                         headers={'Authorization': auth})
        r.json()
