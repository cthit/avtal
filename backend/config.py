import os

# SECURITY
API_KEY = os.environ.get('API_KEY', 'SECRETKEY')

# POSTGRES SETTINGS
POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'example')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_POST = os.environ.get('POSTGRES_PORT', '5432')
POSTGRES_DB = os.environ.get('POSTGRES_DB', 'postgres')

# GAMMA
FRONTEND_CLIENT_ID = os.environ.get(
    'FRONTEND_CLIENT_ID', '7hAdUEtMo4MgFnA7ZoZ41ohTe1NNRoJmjL67Gf0NIrrBnauyhc')
FRONTEND_CLIENT_SECRET = os.environ.get('FRONTEND_CLIENT_SECRET', 'secret')
FRONTEND_REDIRECT_URI = os.environ.get(
    'FRONTEND_REDIRECT_URI', 'http://localhost:3000/login')
