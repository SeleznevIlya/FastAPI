from dotenv import load_dotenv
import os
from fastapi_mail import ConnectionConfig

load_dotenv()

DB_HOST = os.getenv('POSTGRESQL_LOCALHOST')
DB_PORT = os.getenv('POSTGRESQL_PORT')
DB_USERNAME = os.getenv('POSTGRESQL_USERNAME')
DB_NAME = os.getenv('POSTGRESQL_DATABASE_NAME')
DB_PASSWORD = os.getenv('POSTGRESQL_PASSWORD')

DB_HOST_TEST = os.getenv('POSTGRESQL_LOCALHOST_TEST')
DB_PORT_TEST = os.getenv('POSTGRESQL_PORT_TEST')
DB_USERNAME_TEST = os.getenv('POSTGRESQL_USERNAME_TEST')
DB_NAME_TEST = os.getenv('POSTGRESQL_DATABASE_NAME_TEST')
DB_PASSWORD_TEST = os.getenv('POSTGRESQL_PASSWORD_TEST')

SECRET = os.getenv('SECRET')


conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
    MAIL_FROM=os.getenv('MAIL_FROM'),
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_FROM_NAME="Ilya Seleznev",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=False
)
