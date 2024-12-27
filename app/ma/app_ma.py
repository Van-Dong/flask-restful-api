from app.extension import ma
from app.models import *

class StudentSchema(ma.SQLAlchemyAutoSchema):  # Cần dùng ma.SQLAlchemyAutoSchema thì nó mới có thể lấy các kiểu trong models và xác thực được
                                                # nếu dùng ma.Schema --> không xác thực các kiểu trong model đâu -> khi đó model = Category không có hiệu nghiệm
                                                     # Khi đó ta chỉ khai báo các trường mà không định nghĩa kiểu dữ liệu cho nó
    class Meta:
        model = Student
        fields = ('id', 'name', 'birth_date', 'gender', 'class_name')

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        fields = ('id', 'name')

class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        fields = ('id', 'name')

class BorrowSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Borrow
        fields = ('id', 'book_id', 'student_id', 'borrow_date', 'return_date')

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        fields = ('id', 'name', 'page_count', 'author_id', 'category_id')