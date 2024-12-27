from app.extension import db
from app.models.__base import Base

class Student(Base):
    # __tablename__ = 'student'
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date)
    gender = db.Column(db.String(10))
    class_name = db.Column(db.String(10))

    def __init__(self, name, birth_date, gender, class_name):
        self.name = name
        self.birth_date = birth_date
        self.gender = gender
        self.class_name = class_name







