class Library:
    def __init__(self):
        self.books_list = {}
        self.quantity = 1

    def get_bookslist(self):
        return self.books_list

    def add_book(self, book_name):
        if book_name in self.books_list:
            self.books_list[book_name] = self.books_list[book_name] + 1
        else:
            self.books_list[book_name] = self.quantity
            
    def take_books(self, book_name):
        if (book_name in self.books_list and self.books_list[book_name] > 0):
            self.books_list[book_name] = self.books_list[book_name] - 1
        else:
            print(f"{book_name}  already taken")
        return book_name
