from marshmallow import ValidationError
from sqlalchemy import func

from app.extension import db
from app.ma import BookSchema
from app.models import Book, Author
from flask import request
from flask import jsonify

__all__ = ['add_book']  # chỉ hiệu nghiệm với from module1 import *

book_schema = BookSchema()
books_schema = BookSchema(many=True)

def add_book():
    data = request.json  #
    if (data and ('name' in data) and ('page_count' in data)
        and ('author_id' in data) and ('category_id' in data)):
        name = data['name']
        page_count = data['page_count']
        author_id = data['author_id']
        category_id = data['category_id']

        try:
            new_book = Book(name=name, page_count=page_count, author_id=author_id, category_id=category_id)
            db.session.add(new_book)
            db.session.commit()
            return jsonify({'message': 'Add Success!'})
        except:
            db.session.rollback()
            return jsonify({'message': 'Add Failed!'}), 400
    else:
        return jsonify({'message': 'Request error'}), 400

def get_book_by_id(id):
    book = Book.query.get(id)
    if book:
        return book_schema.jsonify(book)
    else:
        return jsonify({'message': 'Book not found'})

def get_all_books():
    books = Book.query.all()
    if books:
        return books_schema.jsonify(books)
    else:
        return 'No books found'

def update_book_by_id(id):
    book = Book.query.get(id)
    data = request.json
    if book:
        try:
            # Load chỉ những trường cần thiết (sử dụng partial)
            updated_data = book_schema.load(data=data)

            # Cập nhật các trường
            for key, value in updated_data.items():
                setattr(book, key, value)

            db.session.commit()
            return book_schema.jsonify(book)
        except ValidationError as e:
            db.session.rollback()
            return {'error': e.messages}, 500

        # if data and "page_count" in data:
        #     try:
        #         book.page_count = data['page_count']
        #         db.session.commit()
        #         return book_schema.jsonify(book)
        #     except:
        #         db.session.rollback()
        #         return "Can not update book"
    else:
        return "Not found books"


def delete_by_id(id):
    book = Book.query.get(id)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
            return "Delete success"
        except:
            db.session.rollback()
            return "Can not delete book"
    else:
        return "Not found books"