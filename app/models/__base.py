# import uuid
from app.extension import db

class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)  # default: giá trị mặc định -> có thể nhận 1 giá trị hoặc một hàm gọi
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return '<id {}>'.format(self.id)
