class Student:
    def __init__(self):
        self.student_list = {}
        self.books = {}

    def get_student_list(self):
        return self.student_list
    
    def get_books(self):
        return self.books

    def add_student(self, name, id):
        if id in self.student_list:
            print("that's student id already exist")
        else:
            self.student_list[id] = name

    def add_books(self, book_name, books_list, id):
        if book_name in books_list and books_list[book_name] > 0:
            self.books[id] = {self.student_list[id]: book_name}
    
    def return_books(self, book_name, books_list, id):
        if book_name in books_list and id in self.books:
            self.books.pop(id)
