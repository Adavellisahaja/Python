# @title Task 3
# Library Management System(eg: Student, Book, Faculty, Department etc.)(Use class, Inheritance, Method Overriding concepts)
class Library():
    __books_list = []
    books_issued = []
    students_list = []

    def __init__(self, library_status=True):
        self.library_status = library_status

    def add_book(self, book_object: 'Book'):
        Library.__books_list.append(book_object)

    def print_books_name(self=None):
        for i in Library.__books_list:
            print(i.book_name)

    def print_students_name(self=None):
        for i in Library.students_list:
            print(i.name)

    def issue_book(self, student_object: 'Student', book_object: 'Book'):
        books_issued.append([student_object, book_object])

    def return_book(self, student_object: 'Student', book_object: 'Book'):
        books_issued.remove([student_object, book_object])


class Student(Library):
    def __init__(self, name, id, email, department):
        Library.__init__(self)
        Library.students_list.append(self)
        self.name = name
        self.id = id
        self.email = email
        self.department = department

    def issue_book(self, book_object: 'Book'):
        Library.books_issued.append([self, book_object])

    def return_book(self, book_object: 'Book'):
        if [self, book_object] in Library.books_issued:
            Library.books_issued.remove([self, book_object])
        else:
            print('Book not issued')


class Book(Library):
    def __init__(self, book_id, book_name, book_author=''):
        Library.__init__(self)
        self.book_id = book_id
        self.book_name = book_name
        self.book_author = book_author

    def add_book(self):
        Library._Library__books_list.append(self)


s1 = Student("zeal", '123', 'abc@m.com', 'sce')
s2 = Student("sahaja", '234', 'qwe@m.com', 'sce')
s3 = Student("shreevali", '345', 'asd@m.com', 'sce')
b1 = Book(1, 'iot');
b1.add_book()
b2 = Book(2, "science");
b2.add_book()
b3 = Book(3, "maths");
b3.add_book()

Library.print_books_name()
print()
Library.print_students_name()
s1.issue_book(b1)
s1.return_book(b1)
print(Library.books_issued)