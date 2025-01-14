import os
from dotenv import load_dotenv  # library python-dotenv

load_dotenv()

SECRET_KEY = os.getenv("KEY")
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False