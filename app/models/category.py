from app.models.__base import Base
from app.extension import db

class Category(Base):
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name