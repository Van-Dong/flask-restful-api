from app.models.__base import Base
from app.extension import db

class Book(Base):
    # __tablename__ = 'student'
    name = db.Column(db.String(100), nullable=False)
    page_count = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __init__(self, name, page_count, author_id, category_id):
        self.name = name
        self.page_count = page_count
        self.author_id = author_id
        self.category_id = category_id