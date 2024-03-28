import pickle
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

def save_to_file(books, filename):
    with open(filename,'wb') as f:
        pickle.dump(books,f)

def load_books_from_file(filename):
    with open(filename,'rb') as f:
        books = pickle.load(f)
    return books

book1 = Book("Seven seas","Harper Lee",1960)
book2 = Book("Wonder of world","George",1946)

books_list = [book1,book2]
save_to_file(books_list,'books_data.pickle')
loaded_books = load_books_from_file('books_data.pickle')

print("\n Loaded books are:")
for book in loaded_books:
    print(book)