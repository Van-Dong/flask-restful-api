# pip install flask-sqlalchemy
# pip install flask-migrate  # Để quản lý version db và tạo db
# flask_marshmallow  # Validate data + convert data
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()