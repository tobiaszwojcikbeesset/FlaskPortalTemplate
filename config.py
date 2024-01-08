from dotenv import load_dotenv
from os import getenv
load_dotenv()


SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI','sqlite:///db.sqlite3')
SECRET_KEY = getenv('SECRET_KEY', 'simplesecredkeyButNotSimple123')
PORT = getenv('PORT', "0.0.0.0")
HOST = getenv('HOST',"5010")
DEBUG = getenv('DEBUG', False) 
SALT = getenv('SALT',"om7c34tqc3{}khweehfe")
MAIN_EMAIL = getenv('MAIN_EMAIL','email@example.com')
ADMIN_INITIAL_PASSWORD = getenv('ADMIN_INITIAL_PASSWORD', 'password')
