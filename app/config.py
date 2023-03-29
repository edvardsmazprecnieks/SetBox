from dotenv import load_dotenv
from os import environ

load_dotenv()

DATABASE_URI = environ.get('DATABASE_URL')