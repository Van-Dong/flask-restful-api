from app.models.__base import Base
from app.extension import db

class Borrow(Base):
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    borrow_date = db.Column(db.Date)
    return_date = db.Column(db.Date)

    def __init__(self, book_id, student_id, borrow_date, return_date):
        self.book_id = book_id
        self.student_id = student_id
        self.borrow_date = borrow_date
        self.return_date = return_date
