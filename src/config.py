from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv('POSTGRESQL_LOCALHOST')
DB_PORT = os.getenv('POSTGRESQL_PORT')
DB_USERNAME = os.getenv('POSTGRESQL_USERNAME')
DB_NAME = os.getenv('POSTGRESQL_DATABASE_NAME')
DB_PASSWORD = os.getenv('POSTGRESQL_PASSWORD')




