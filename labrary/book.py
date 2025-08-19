class Book:
    def __init__(self, code, title, author_last_name, author_first_name, knowledge_area, publisher, assigned_section):
        self.code = code
        self.title = title
        self.author_last_name = author_last_name
        self.author_first_name = author_first_name
        self.knowledge_area = knowledge_area
        self.publisher = publisher
        self.assigned_section = assigned_section

class Library:
    def __init__(self):
        self.books = []

    def save_book(self, book):
        self.books.append(book)

    def modify_book(self, code, updated_book):
        for index, book in enumerate(self.books):
            if book.code == code:
                self.books[index] = updated_book
                return True
        return False

    def list_books(self):
        return self.books

    def search_book(self, code):
        for book in self.books:
            if book.code == code:
                return book
        return None

    def delete_book(self, code):
        for index, book in enumerate(self.books):
            if book.code == code:
                del self.books[index]
                return True
        return False