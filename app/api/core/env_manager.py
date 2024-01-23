import os
from dotenv import load_dotenv

load_dotenv()

class EnvManager:
    SQLALCHEMY_DATABASE_URL: str = os.environ.get('SQLALCHEMY_DATABASE_URL')
