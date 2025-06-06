# create class for BOOK
class Book:
    def __init__(self, author, title, num_of_pages):
        self.author = author
        self.title = title
        self.num_of_pages = num_of_pages

# create class for SHELF
class Shelf:
    def __init__(self):
        self.books = []
        self.is_shelf_full = False  
    
    def add_book(self, book):
        if len(self.books) < 5:
            self.books.append(book)
            if len(self.books) == 5:
                self.is_shelf_full = True
            else:
                self.is_shelf_full = False
        else:
            print("Shelf is full")
        
    def replace_books(self, pos1, pos2):
        if pos1 < len(self.books) and pos2 < len(self.books):
            self.books[pos1], self.books[pos2] = self.books[pos2], self.books[pos1]
        else:
            print("One of the positions is invalid")

# create class for READER
class Reader:
    def __init__(self, reader_id, name):
        self.reader_id = reader_id
        self.name = name
        self.books_read = []

    def read_book(self, book_title):
        self.books_read.append(book_title)

# create class for LIBRARY
class Library:
    def __init__(self):
        self.shelves = [Shelf(), Shelf(), Shelf()]
        self.readers = []

    def is_there_place_for_new_book(self):
        for shelf in self.shelves:
            if len(shelf.books) < 5:
                return True
        return False

    def add_new_book(self, book):
        for shelf in self.shelves:
            if len(shelf.books) < 5:
                shelf.add_book(book)
                return
        print("No space to add a new book")

    def delete_book(self, title: str):
        for shelf in self.shelves:
            for i, book in enumerate(shelf.books):
                if book.title == title:
                    shelf.books.pop(i)
                    shelf.is_shelf_full = False
                    print("Book deleted")
                    return
        print("Book not found")

    def register_reader(self, name, reader_id):
        self.readers.append(Reader(reader_id, name))

    def remove_reader(self, name):
        for i in range(len(self.readers)):
            if self.readers[i].name == name:
                self.readers.pop(i)
                print("Reader removed")
                return
        print("Reader not found")

    def search_books_by_author(self, author):
        found_books = []
        for shelf in self.shelves:
            for book in shelf.books:
                if book.author == author:
                    found_books.append(book.title)
        return found_books
      
#Program Requirments:
library = Library()

# הוספת שני ספרים כברירת מחדל לכל מדף
default_books = [
    Book("Mark Twain", "Tom Sawyer", 274),
    Book("Brothers Grimm", "Snow White", 96)
]

for shelf in library.shelves:
    for book in default_books:
        shelf.add_book(book)
      
#an infinite loop until the user chooses to EXIT 
while True:
    print("Menu:")
    print("1. Add book")
    print("2. Delete book")
    print("3. Register reader")
    print("4. Remove reader")
    print("5. Search books by author")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        author = input("Enter author name: ")
        title = input("Enter book title: ")
        pages = int(input("Enter number of pages: "))
        library.add_new_book(Book(author, title, pages))

    elif choice == "2":
        title = input("Enter book title to delete: ")
        library.delete_book(title)

    elif choice == "3":
        name = input("Enter reader name: ")
        reader_id = int(input("Enter reader ID: "))
        library.register_reader(name, reader_id)

    elif choice == "4":
        name = input("Enter reader name to remove: ")
        library.remove_reader(name)

    elif choice == "5":
        author = input("Enter author name to search: ")
        books = library.search_books_by_author(author)
        if books:
            print("Books found:", books)
        else:
            print("No books found by that author.")

    elif choice == "6":
        print("Goodbye!")
        break



