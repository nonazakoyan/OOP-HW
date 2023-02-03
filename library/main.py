import library
import student
import random

def obj_init(lib, person):
    for id, name in enumerate(student_names, 1):
        person.add_student(name, id)
    for i in range(10):
        lib.add_book(random.choice(books_name))

def to_take(book_name, books_list, stud_id):
    person.add_books(book_name, books_list, stud_id)
    lib.take_books(book_name)

def to_return(book_name, books_list, stud_id):
    lib.add_book(book_name)
    person.return_books(book_name, books_list, stud_id)

random.seed(0)
lib = library.Library()
person = student.Student()

books_name = ['ooad', 'python', 'c++', 'js']
student_names = ['Bob', 'James', 'James', 'Bob', 'Sara', 'Kya']
book_name = random.choice(books_name)
obj_init(lib, person)
print(lib.get_bookslist())

to_take('ooad', lib.get_bookslist(), 1)
to_take('ooad', lib.get_bookslist(), 2)
to_take('ooad', lib.get_bookslist(), 3)
to_take('ooad', lib.get_bookslist(), 4)
to_take('python', lib.get_bookslist(), 5)
to_take('c++', lib.get_bookslist(), 6)
to_return('ooad', lib.get_bookslist(), 1)

print(f'id student book {person.get_books()}')
print(f"list of books {lib.get_bookslist()}")
