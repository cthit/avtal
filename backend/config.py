import os

# POSTGRES SETTINGS
POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'example')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'db')
POSTGRES_POST = os.environ.get('POSTGRES_PORT', '5432')
POSTGRES_DB = os.environ.get('POSTGRES_DB', 'db')

