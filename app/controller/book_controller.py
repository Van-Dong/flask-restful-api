from flask import Blueprint
import app.service.book_service as book_service

books = Blueprint('books', __name__)

@books.route("/books", methods=['GET'])
def get_books():
    return "All books"

@books.route("/book-management/book", methods=['POST'])
def add_book():
    return book_service.add_book()

@books.get('/book-management/book/<int:id>')
def get_book_by_id(id):
    return book_service.get_book_by_id(id)

@books.get("/book-management/books")
def get_all_books():
    return book_service.get_all_books()

@books.put("/book-management/book/<int:id>")
def update_book(id):
    return book_service.update_book_by_id(id)

@books.delete("/book-management/book/<int:id>")
def delete_book(id):
    return book_service.delete_by_id(id)
